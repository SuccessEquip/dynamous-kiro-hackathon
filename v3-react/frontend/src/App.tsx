import { COREFramework } from './components/COREFramework'
import { ThemeProvider } from './components/theme-provider'

function App() {
  return (
    <ThemeProvider defaultTheme="light" storageKey="core-framework-theme">
      <div className="min-h-screen bg-background">
        <COREFramework />
      </div>
    </ThemeProvider>
  )
}

export default App
