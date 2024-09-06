import React from "react";
import CarouselComponent from "./CarouselComponent.jsx";

const CarCard = (props) => {

    let img = props.carCard.image_links.split(/,/)
    let card_commercial = props.carCard.card_commercial.split(' ')
    let card_params = props.carCard.card_params.split(/,/)
    let first_similar_ad_prices = props.carCard.first_similar_ad_price.split('.')
    let second_similar_ad_prices = props.carCard.second_similar_ad_price.split('.')
    let third_similar_ad_prices = props.carCard.third_similar_ad_price.split('.')
    let fourth_similar_ad_prices = props.carCard.fourth_similar_ad_price.split('.')
    let fifth_similar_ad_prices = props.carCard.fifth_similar_ad_price.split('.')
    let sixth_similar_ad_prices = props.carCard.sixth_similar_ad_price.split('.')
    let seventh_similar_ad_prices = props.carCard.seventh_similar_ad_price.split('.')


    return(
        <div>
         <div class="car-card-item">
         <table class="car-card-item-table">
            <div class="J">{props.carCard.card_header}</div>
            <div class="K">добавлено {props.carCard.date_added}</div>
            <div class="L"><CarouselComponent class="carousel-component" img={img}/></div>
            <div class="M">
                <div class="car-card-price-primary">{props.carCard.card_price_primary} p.</div>
                <div class="car-card-price-secondary">≈ {props.carCard.card_price_secondary} $</div>
                <div class="car-card-commercial">{card_commercial[0]} {card_commercial[1]}
                           ≈ {card_commercial[2]} {card_commercial[3]} {card_commercial[4]} {card_commercial[5]}</div>
            </div>
            <div class="N"><div class="car-card-params">{card_params[0]}, {card_params[1]}, {card_params[2]}, {card_params[3]},</div>
                           <div>{card_params[4]}</div>
                           <div class="car-card-short-description">{props.carCard.card_short_description}</div>
                           <div class="car-card-short-modification"> {props.carCard.card_short_modification}</div>
                           <div><hr></hr></div>
                           <div class="car-card-location">{props.carCard.card_location}</div>
                           </div>
        </table>
        <div class="car-card-description-title">Описание</div>
        <div class="car-card-card-comment-text">{props.carCard.card_comment_text}</div>
        <div class="car-card-title-exchange">{props.carCard.card_exchange}</div>
        <div><hr></hr></div>
        <table>
           <td class="td-car-card-description">
               <div class="car-card-title">Экстерьер</div>
               <tr>{props.carCard.exterior}</tr>
               <div class="car-card-title">Системы безопасности</div>
               <tr>{props.carCard.security_systems}</tr>
               <div class="car-card-title">Подушки</div>
               <tr>{props.carCard.pillows}</tr>
           </td>
           <td class="td-car-card-description">
               <div class="car-card-title">Системы помощи</div>
               <tr>{props.carCard.help_systems}</tr>
               <div class="car-card-title">Интерьер</div>
               <tr>{props.carCard.interior}</tr>
            </td>
            <td class="td-car-card-description">
               <div class="car-card-title">Комфорт</div>
               <tr>{props.carCard.comfort}</tr>
               <div class="car-card-title">Обогрев</div>
               <tr>{props.carCard.heating}</tr>
            </td>
            <td class="td-car-card-description">
               <div class="car-card-title">Климат</div>
               <tr>{props.carCard.climate}</tr>
               <div class="car-card-title">Мультимедия</div>
               <tr>{props.carCard.multimedia}</tr>
            </td>
            </table>
        </div>
        <table class="car-card-credit-and-leasing-table">
            <td>
                <img class="car-card-finance-image" src={props.carCard.card_finance_image} alt="No image"/>
            </td>
            <td><div class="car-card-finance-title">Кредиты и лизинг на покупку</div>
                <div class="car-card-finance-description">{props.carCard.card_finance_description}</div>
            </td>
        </table>
        <div class="car-card-similar-ads-title">Похожие объявления</div>
        <div>
            <div class="car-card-similar-ads-title">{props.carCard.card_average_price}</div>
            <div class="car-card-grey">средняя цена</div>
            <div class="car-card-grey">без учёта пробега и комплектации</div>
        </div>
        <table class="car-card-similar-cars-table">
            <tr>
                <td class="car-card-similar-car">
                    <div class="car-card-similar-ad-foto-div">
                        <img class="car-card-similar-ad-foto" src={props.carCard.first_similar_ad_photo} alt="No image"/>
                    </div>
                        <div class="car-card-similar-ad-title">{props.carCard.first_similar_ad_title}</div>
                        <div>
                        <td class="car-card-similar-ad-price-byn">{first_similar_ad_prices[0]}</td>
                        <td class="car-card-similar-ad-price-usd"> ≈{first_similar_ad_prices[1]}</td>
                        </div>
                        <div class="car-card-similar-ad-params">{props.carCard.first_similar_ad_params}</div>
                    </td>
                    <td class="car-card-similar-car">
                    <div class="car-card-similar-ad-foto-div">
                        <img class="car-card-similar-ad-foto" src={props.carCard.second_similar_ad_photo} alt="No image"/>
                    </div>
                        <div class="car-card-similar-ad-title">{props.carCard.second_similar_ad_title}</div>
                        <div>
                        <td class="car-card-similar-ad-price-byn">{second_similar_ad_prices[0]}</td>
                        <td class="car-card-similar-ad-price-usd"> ≈{second_similar_ad_prices[1]}</td>
                        </div>
                        <div class="car-card-similar-ad-params">{props.carCard.second_similar_ad_params}</div>
                    </td>
                    <td class="car-card-similar-car">
                    <div class="car-card-similar-ad-foto-div">
                        <img class="car-card-similar-ad-foto" src={props.carCard.third_similar_ad_photo} alt="No image"/>
                    </div>
                        <div class="car-card-similar-ad-title">{props.carCard.third_similar_ad_title}</div>
                        <div>
                        <td class="car-card-similar-ad-price-byn">{third_similar_ad_prices[0]}</td>
                        <td class="car-card-similar-ad-price-usd"> ≈{third_similar_ad_prices[1]}</td>
                        </div>
                        <div class="car-card-similar-ad-params">{props.carCard.third_similar_ad_params}</div>
                    </td>
            </tr>
            </table>
            <table class="car-card-similar-cars-table">
            <tr>
                <td class="car-card-similar-car">
                    <div class="car-card-similar-ad-foto-div-small">
                        <img class="car-card-similar-ad-foto" src={props.carCard.fourth_similar_ad_photo} alt="No image"/>
                    </div>
                        <div class="car-card-similar-ad-title">{props.carCard.fourth_similar_ad_title}</div>
                        <div>
                        <td class="car-card-similar-ad-price-byn">{fourth_similar_ad_prices[0]}</td>
                        <td class="car-card-similar-ad-price-usd"> ≈{fourth_similar_ad_prices[1]}</td>
                        </div>
                        <div class="car-card-similar-ad-params">{props.carCard.fourth_similar_ad_params}</div>
                    </td>
                    <td class="car-card-similar-car">
                    <div class="car-card-similar-ad-foto-div-small">
                        <img class="car-card-similar-ad-foto" src={props.carCard.fifth_similar_ad_photo} alt="No image"/>
                    </div>
                        <div class="car-card-similar-ad-title">{props.carCard.fifth_similar_ad_title}</div>
                        <div>
                        <td class="car-card-similar-ad-price-byn">{fifth_similar_ad_prices[0]}</td>
                        <td class="car-card-similar-ad-price-usd"> ≈{fifth_similar_ad_prices[1]}</td>
                        </div>
                        <div class="car-card-similar-ad-params">{props.carCard.fifth_similar_ad_params}</div>
                    </td>
                    <td class="car-card-similar-car">
                    <div class="car-card-similar-ad-foto-div-small">
                        <img class="car-card-similar-ad-foto" src={props.carCard.sixth_similar_ad_photo} alt="No image"/>
                    </div>
                        <div class="car-card-similar-ad-title">{props.carCard.sixth_similar_ad_title}</div>
                        <div>
                        <td class="car-card-similar-ad-price-byn">{sixth_similar_ad_prices[0]}</td>
                        <td class="car-card-similar-ad-price-usd"> ≈{sixth_similar_ad_prices[1]}</td>
                        </div>
                        <div class="car-card-similar-ad-params">{props.carCard.sixth_similar_ad_params}</div>
                    </td>
                    <td class="car-card-similar-car">
                    <div class="car-card-similar-ad-foto-div-small">
                        <img class="car-card-similar-ad-foto" src={props.carCard.seventh_similar_ad_photo} alt="No image"/>
                    </div>
                        <div class="car-card-similar-ad-title">{props.carCard.seventh_similar_ad_title}</div>
                        <div>
                        <td class="car-card-similar-ad-price-byn">{seventh_similar_ad_prices[0]}</td>
                        <td class="car-card-similar-ad-price-usd"> ≈{seventh_similar_ad_prices[1]}</td>
                        </div>
                        <div class="car-card-similar-ad-params">{props.carCard.seventh_similar_ad_params}</div>
                    </td>
            </tr>
            </table>
        </div>
    )
}

export default CarCard;

