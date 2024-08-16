import React from 'react'
import { useEffect,useState } from 'react'
import axios from 'axios'
import CarsTable from "../components/CarsTable"
import CheckedCar from '../components/CheckedCar'

const API_URL_CHECKED_CAR_PAGE = 'http://127.0.0.1:8000/user_car_relations/'
const API_URL_CAR_PAGE = 'http://127.0.0.1:8000/cars/'

const Home = ({cars}) => {
    const [username, setUsername] = useState('');
    const [userId, setUserId] = useState('');
    const [checkedCarsId, setCheckedCarsId] = useState([])
    const [checkedCars, setCheckedCars] = useState([])

    async function getCheckedCarsId(user) {
        const response = await axios.get(API_URL_CHECKED_CAR_PAGE+'?user__in='+user)
        setCheckedCarsId(response.data)
    }

    async function getCheckedCars(carsId) {
        const response = await axios.get(API_URL_CAR_PAGE +'?id__in='+carsId)
        setCheckedCars(response.data)
    }

    const checkedId = checkedCarsId.map(checkedCar => {
            return checkedCar.car+','})

    useEffect(() => {
        if(localStorage.getItem('access_token') ===null){
          window.location.href = '/login'

        }else{
          (async () =>{
            try{
              const {data} = await axios.get(
                'http://127.0.0.1:8000/home/',{
                  headers:{
                    'Content-Type':'application/json'
                  },
                  withCredentials:true,
                }
              );
              setUsername(data.username)
              setUserId(data.userId)
            }
            catch (e){
              console.log('not auth')
            }
          })()};
            getCheckedCarsId(userId)
            getCheckedCars(checkedId)
          },[userId]);

    return (
        <div className="form-signin mt-5 text-center">
            <h3>Добро пожаловать, {username}!</h3>
        <div>{userId}</div>
            <div>{checkedId}</div>
            <CarsTable carsCount={checkedCars.length} cars={checkedCars}/>
      </div>
    )
    }

export default Home




