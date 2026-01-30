#!/bin/bash
# CORE Framework Launcher - Unix/Linux/macOS

set -e

# Colors
CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check Python (try python3 first, then python, then py)
check_python() {
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
    elif command -v py &> /dev/null; then
        PYTHON_CMD="py"
    else
        echo -e "${RED}ERROR: Python is not installed or not in PATH.${NC}"
        echo -e "${YELLOW}Please install Python 3.8+ from python.org${NC}"
        return 1
    fi
    
    VERSION=$($PYTHON_CMD --version 2>&1)
    echo -e "${GREEN}Found: $VERSION${NC}"
    return 0
}

# Install dependencies
install_deps() {
    local req_file="$1"
    if [ -f "$req_file" ]; then
        echo -e "${YELLOW}Installing dependencies...${NC}"
        $PYTHON_CMD -m pip install -r "$req_file" --quiet
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}Dependencies installed successfully.${NC}"
        else
            echo -e "${RED}Failed to install dependencies.${NC}"
            return 1
        fi
    fi
}

# Launch v1
launch_v1() {
    echo -e "\n${CYAN}Launching v1 - HTML/CSS/JS...${NC}"
    cd "$SCRIPT_DIR/v1-html"
    
    if [[ "$OSTYPE" == "darwin"* ]]; then
        open index.html
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        xdg-open index.html 2>/dev/null || sensible-browser index.html 2>/dev/null || echo -e "${YELLOW}Please open v1-html/index.html in your browser${NC}"
    fi
    
    echo -e "${GREEN}Browser should open automatically.${NC}"
    read -p "Press Enter to continue..."
}

# Launch v2
launch_v2() {
    echo -e "\n${CYAN}Launching v2 - Python TUI...${NC}"
    cd "$SCRIPT_DIR/v2-python"
    
    echo -e "${YELLOW}Checking Python...${NC}"
    check_python || return 1
    
    # Check/create virtual environment
    if [ ! -d "venv" ] || [ ! -f "venv/bin/python" ]; then
        echo -e "${YELLOW}Creating virtual environment...${NC}"
        $PYTHON_CMD -m venv venv 2>&1 | tee /tmp/venv_error.txt
        
        if [ $? -ne 0 ] || grep -q "python3-venv" /tmp/venv_error.txt; then
            echo -e "${YELLOW}Installing python3-venv package...${NC}"
            sudo apt install -y python3-venv
            if [ $? -ne 0 ]; then
                echo -e "${RED}Failed to install python3-venv.${NC}"
                read -p "Press Enter to continue..."
                return 1
            fi
            echo -e "${YELLOW}Recreating virtual environment...${NC}"
            rm -rf venv
            $PYTHON_CMD -m venv venv
            if [ $? -ne 0 ]; then
                echo -e "${RED}Failed to create virtual environment.${NC}"
                read -p "Press Enter to continue..."
                return 1
            fi
        fi
    fi
    
    # Use venv's python directly
    VENV_PYTHON="venv/bin/python"
    
    # Verify venv has pip, if not reinstall python3-venv
    if ! $VENV_PYTHON -m pip --version &>/dev/null; then
        echo -e "${YELLOW}Virtual environment incomplete, installing python3-venv...${NC}"
        sudo apt install -y python3-venv
        if [ $? -ne 0 ]; then
            echo -e "${RED}Failed to install python3-venv.${NC}"
            read -p "Press Enter to continue..."
            return 1
        fi
        echo -e "${YELLOW}Recreating virtual environment...${NC}"
        rm -rf venv
        $PYTHON_CMD -m venv venv
        if [ $? -ne 0 ]; then
            echo -e "${RED}Failed to create virtual environment.${NC}"
            read -p "Press Enter to continue..."
            return 1
        fi
    fi
    
    # Check if textual is installed in venv
    if ! $VENV_PYTHON -c "import textual" 2>/dev/null; then
        echo -e "${YELLOW}Installing dependencies in virtual environment...${NC}"
        $VENV_PYTHON -m pip install -r requirements.txt
        if [ $? -ne 0 ]; then
            echo -e "${RED}Failed to install dependencies.${NC}"
            read -p "Press Enter to continue..."
            return 1
        fi
        echo -e "${GREEN}Dependencies installed.${NC}"
    else
        echo -e "${GREEN}Dependencies OK.${NC}"
    fi
    
    echo -e "\n${CYAN}Starting CORE Framework TUI...${NC}"
    $VENV_PYTHON -m core_framework.main
}

# Launch v3
launch_v3() {
    echo -e "\n${CYAN}Launching v3 - React + Supabase...${NC}"
    cd "$SCRIPT_DIR/v3-react/frontend"
    
    # Check Node.js
    if ! command -v node &> /dev/null; then
        echo -e "${RED}ERROR: Node.js is not installed.${NC}"
        echo -e "${YELLOW}Please install Node.js 18+ from nodejs.org${NC}"
        read -p "Press Enter to continue..."
        return 1
    fi
    
    NODE_VERSION=$(node --version)
    echo -e "${GREEN}Found Node.js: $NODE_VERSION${NC}"
    
    # Check if node_modules exists
    if [ ! -d "node_modules" ]; then
        echo -e "${YELLOW}Installing dependencies (this may take a minute)...${NC}"
        npm install
    else
        echo -e "${GREEN}Dependencies OK.${NC}"
    fi
    
    echo -e "\n${CYAN}Starting development server...${NC}"
    echo -e "${GREEN}Server will run at http://localhost:5173${NC}"
    echo -e "${YELLOW}Press Ctrl+C to stop${NC}\n"
    
    # Open browser after delay
    (sleep 3 && if [[ "$OSTYPE" == "darwin"* ]]; then
        open http://localhost:5173
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        xdg-open http://localhost:5173 2>/dev/null
    fi) &
    
    npm run dev
}

# Main menu
while true; do
    clear
    echo -e "${CYAN}╔════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║   CORE Framework Launcher          ║${NC}"
    echo -e "${CYAN}╚════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${GREEN}1.${NC} v1 - HTML/CSS/JS (No dependencies)"
    echo -e "${GREEN}2.${NC} v2 - Python TUI (Terminal interface)"
    echo -e "${GREEN}3.${NC} v3 - React + Supabase (Full-featured)"
    echo -e "${RED}4.${NC} Exit"
    echo ""
    read -p "Enter your choice (1-4): " choice
    
    case $choice in
        1) launch_v1 ;;
        2) launch_v2 ;;
        3) launch_v3 ;;
        4) echo -e "\n${CYAN}Thank you for using CORE Framework!${NC}"; exit 0 ;;
        *) echo -e "${RED}Invalid choice. Press Enter to try again...${NC}"; read ;;
    esac
done
