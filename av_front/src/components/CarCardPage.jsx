import React, {useState, useEffect} from 'react';
import {useLocation} from 'react-router-dom';
import axios from 'axios';
import CarCard from "./CarCard";

const API_URL_CAR_PAGE = 'http://127.0.0.1:8000/cars/'

const CarCardPage = () => {

    const location = useLocation()
    const [carId, setCarId] = useState(location.state.id)
    const [cars, setCars] = useState([])

    async function getCars(carId) {
        const response = await axios.get(API_URL_CAR_PAGE+'?id__in='+carId)
        setCars(response.data)
    }

    useEffect(() => {
        getCars(carId)
    },[])

    return(
        <div>
            {cars.map(car => <CarCard carCard={car} key={car.id}/>)}
        </div>

        )
    }

export default CarCardPage;