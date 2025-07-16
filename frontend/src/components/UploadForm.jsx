import { useState } from "react"
import axios from 'axios'

function UploadForm() {
    const [file, setFile] = useState(null)
    const [instruction, setInstruction] = useState('')
    const [downloading, setDownloading] = useState(false)

    const handleSubmit = async (e) => {
        e.preventDefault()
        if (!file || !instruction) return alert('Completa todos los campos')
        
        const formData = new FormData()
        formData.append('file', file)
        formData.append('instruction', instruction)

        setDownloading(true)

        try {
            const response = await axios.post('http://localhost:8000/api/excel/process/', formData, {
                responseType: 'blob',
            })

            const blob = new Blob([response.data], {type: response.headers['Content-Type']})
            const url = window.URL.createObjectURL(blob)
            const link = document.createElement('a')
            link.href = url
            link.setAttribute('download', 'resultado.xlsx')
            document.body.appendChild(link)
            link.click()
            link.remove()
        } catch (err) {
            alert('Error al procesar el archivo')
        } finally {
            setDownloading(false)
        }
    }

    return (
        <form onSubmit={handleSubmit} style={{display:'flex', flexDirection:'column', gap:'1rem'}}>
            <input type="file" accept=".xlsx, .xls" onChange={(e) => setFile(e.target.files[0])}/>
            <textarea value={instruction} onChange={(e) => setInstruction(e.target.value)} placeholder="Describe qué hacer..."/>
            <button type="submit" disabled={downloading}>{downloading ? 'Procesando...' : 'Enviar'}</button>
        </form>
    )
}

export default UploadForm