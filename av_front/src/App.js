import './App.css';
import React, {useState, useEffect} from "react";
import GeneralPage from "./components/GeneralPage";
import GeneralItem from "./components/GeneralItem"
import Car from "./components/Car"
import SelectedCarMarkPage from "./components/SelectedCarMarkPage"
import axios from "axios";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import GeneralLineTable from "./components/GeneralLineTable"
import Login from "./authComponents/Login";
import Home from './authComponents/Home';
import Logout from './authComponents/Logout';
import Register from './authComponents/Register'



const API_URL_GENERAL_PAGE = 'http://127.0.0.1:8000/general/'
const API_URL_CAR_PAGE = 'http://127.0.0.1:8000/cars/'
const API_URL_MODEL_PAGE = 'http://127.0.0.1:8000/models/'


function App() {
    const [generalItems, setGeneralItems] = useState([])
    const [cars, setCars] = useState([])
    const [models, setModels] = useState([])
    const [mark, setMark] = useState(null)

    async function getGeneralItems() {
        const response = await axios.get(API_URL_GENERAL_PAGE)
        setGeneralItems(response.data)
    }

    async function getCars() {
        const response = await axios.get(API_URL_CAR_PAGE)
        setCars(response.data)
    }

    async function getModels() {
        const response = await axios.get(API_URL_MODEL_PAGE)
        setModels(response.data)
    }

    useEffect(() => {
        getGeneralItems()}, [])

    useEffect(() => {
        getCars()}, [])

    useEffect(() => {
        getModels()}, [])

    return (
        <div className="App">

            <Routes>
                <Route path="/GeneralPage" element={<GeneralPage generalItems={generalItems} cars={cars} models={models}/>} />
                <Route path="/SelectedCar" element={<SelectedCarMarkPage generalItems={generalItems} models={models} cars={cars}/>} />
                <Route path="/" element={<Home/>}/>
                <Route path="/login" element={<Login/>}/>
                <Route path="/logout" element={<Logout/>}/>
                <Route path="/register" element={<Register/>}/>
            </Routes>

        </div>

    );
}

export default App;
