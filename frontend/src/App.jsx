import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom'
// Import components
import UploadForm from './components/UploadForm'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<UploadForm />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App