// Import axios
import axios from 'axios'

// Config axios
const ExcelAgentAPI = axios.create({
    baseURL: 'http://localhost:8000/'
})

export default ExcelAgentAPI