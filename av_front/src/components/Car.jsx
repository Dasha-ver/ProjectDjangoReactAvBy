import React from "react";
import Checkbox from "@mui/material/Checkbox";
import BookmarkBorderIcon from "@mui/icons-material/BookmarkBorder";
import BookmarkIcon from "@mui/icons-material/Bookmark";
import { green, blue } from "@mui/material/colors";
import useState from 'react'
import axios from 'axios'


const Car = (props) => {

    const [isChecked, setChecked] = React.useState(false)
    const [username, setUsername] = React.useState('');
    const [userId, setUserId] = React.useState('');
    let img = props.car.image_links.split(/,/)
    let card_params = props.car.card_params.split(/,/)
    let card_commercial = props.car.card_commercial.split(' ')

    function handleChange(event) {
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
          })()}
        setChecked(event.target.checked);
}

    return(

        <table class="car-item-table">
{/*             <div>{username}</div> */}
            <div class="A"><img class="car-item-img" src={img[0]} alt="No image"/></div>
            <div class="B">{props.car.mark_link_text} {props.car.model_link_text}</div>
            <div class="C"><div>{card_params[0]},</div>
                           <div>{card_params[1]}, {card_params[2]}, {card_params[3]},</div>
                           <div>{card_params[4]}</div></div>
            <div class="D"><div>{props.car.card_price_primary} р.</div>
                           <div>≈ {props.car.card_price_secondary} $</div></div>
            <div class="E">
                <Checkbox
                    Icon = {<BookmarkBorderIcon />}
                    checkedIcon = {<BookmarkIcon />}
                    onChange = {handleChange}
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