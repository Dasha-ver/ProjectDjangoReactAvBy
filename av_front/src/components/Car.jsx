import React from "react";


const Car = (props) => {

    let img = props.car.image_links.split(/,/)
    let card_params = props.car.card_params.split(/,/)
    let card_commercial = props.car.card_commercial.split(' ')


    return(

        <table class="car-item-table">
            <div class="A"><img class="car-item-img" src={img[0]} alt="No image"/></div>
            <div class="B">{props.car.mark_link_text} {props.car.model_link_text}</div>
            <div class="C"><div>{card_params[0]},</div>
                           <div>{card_params[1]}, {card_params[2]}, {card_params[3]},</div>
                           <div>{card_params[4]}</div></div>
            <div class="D"><div>{props.car.card_price_primary} р.</div>
                           <div>≈ {props.car.card_price_secondary} $</div></div>
            <div class="E">E</div>
            <div class="F">{props.car.card_comment_text}</div>
            <div class="G"><div>{card_commercial[0]} {card_commercial[1]}</div>
                           <div>≈ {card_commercial[2]} {card_commercial[3]} {card_commercial[4]} {card_commercial[5]}</div>                                              </div>
            <div class="H">{props.car.card_location}</div>



        </table>

    )
}

export default Car;