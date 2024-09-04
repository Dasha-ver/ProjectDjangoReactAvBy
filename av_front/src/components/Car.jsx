import React from "react";
import Checkbox from "@mui/material/Checkbox";
import BookmarkBorderIcon from "@mui/icons-material/BookmarkBorder";
import BookmarkIcon from "@mui/icons-material/Bookmark";
import { blue } from "@mui/material/colors";
import {useState, useEffect} from 'react';
import axios from 'axios';
import CheckedCar from './CheckedCar';
import {useNavigate} from 'react-router-dom';
import CarCardPage from './CarCardPage'

const API_URL_CHECKED_CAR_PAGE = 'http://127.0.0.1:8000/user_car_relations/'

const Car = (props) => {

    const [isChecked, setChecked] = React.useState(false)
    const [checkedCars, setCheckedCars] = React.useState([])
    const [userId, setUserId] = React.useState('')
    let img = props.car.image_links.split(/,/)
    let card_params = props.car.card_params.split(/,/)
    let card_commercial = props.car.card_commercial.split(' ')
    const navigate = useNavigate()


    async function getCheckedCars(user, car) {
        const response = await axios.get(API_URL_CHECKED_CAR_PAGE+'?user__in='+user+'&car__in='+car)
        setCheckedCars(response.data)
    }

    useEffect(() => {
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
              setUserId(data.userId)
            }
            catch (e){
              console.log('not auth')
            }
          })();
        getCheckedCars(userId, props.car.id)
        if(checkedCars.length > 0){
            setChecked(true)}
      },[checkedCars.length, userId, props.car.id]);

    const checkedCarId = checkedCars.map(checkedCar => {
        return checkedCar.id})


    function handleChange(event) {
        if(localStorage.getItem('access_token') ===null){
            window.location.href = '/login'
        }else{
            if(isChecked === false){
              (async () =>{
                try{
                  await fetch(' http://127.0.0.1:8000/user_car_relations/',{
                      method:'POST',
                      headers:{'Content-Type':"application/json"},
                      body: JSON.stringify(
                        {
                          user:userId,
                          car:props.car.id
                        }
                      )
            });
        }
                catch (e){
                  console.log('not auth')
                }
              })()
          }else{
                axios.delete(API_URL_CHECKED_CAR_PAGE+ 'delete/'+checkedCarId+'/')
          }
            setChecked(event.target.checked)
            }
}
    return(

        <table class="car-item-table">
            <div class="A"><img class="car-item-img" src={img[0]} alt="No image"/></div>
            <div class="B">
                <button class="car-name" onClick={() => navigate("/CarCardPage",{state:{id:props.car.id}})}>
                    {props.car.mark_link_text} {props.car.model_link_text}
                </button>
            </div>
            <div class="C"><div>{card_params[0]},</div>
                           <div>{card_params[1]}, {card_params[2]}, {card_params[3]},</div>
                           <div>{card_params[4]}</div></div>
            <div class="D"><div>{props.car.card_price_primary} р.</div>
                           <div>≈ {props.car.card_price_secondary} $</div></div>
            <div class="E">
                <Checkbox
                    Icon = {<BookmarkBorderIcon />}
                    checkedIcon = {<BookmarkIcon />}
                    checked={isChecked}
                    onChange ={handleChange}
                    sx = {{
                       color: blue[500],
                       "&.Mui-checked": {
                          color: blue[200],
                       },
                    }}
                />
            </div>
            <div class="F">{props.car.card_comment_text}</div>
            <div class="G"><div>{card_commercial[0]} {card_commercial[1]}</div>
                           <div>≈ {card_commercial[2]} {card_commercial[3]} {card_commercial[4]} {card_commercial[5]}</div>                                              </div>
            <div class="H">{props.car.card_location}</div>
        </table>

    )
}

export default Car;