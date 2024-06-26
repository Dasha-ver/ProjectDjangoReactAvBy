import React, {useState, useEffect} from 'react';
import {useLocation} from 'react-router-dom';
import general_pic from "../pictures/general-pic.jpg";
import GeneralLineTable from "./GeneralLineTable"
import FindForParamsForm from "./FindForParamsForm"
import CarsTable from "./CarsTable"
import axios from "axios";


const SelectedCarMarkPage = ({generalItems, cars, models}) => {

    const location = useLocation();
    const [mark, setMark] = useState(generalItems.filter(t => t.title === location.state.selectedMark))
    const [markLink, setMarkLink] = useState(location.state.link)
    const [modelLink, setModelLink] = useState("")
    const [selectedCars, setSelectedCars] = useState([])
    const [carsCount, setCarsCount] = useState(location.state.count)
    const [yearFrom, setYearFrom] = useState(null)
    const [yearTo, setYearTo] = useState(null)
    const [priceFrom, setPriceFrom] = useState(0)
    const [priceTo, setPriceTo] = useState(10000000)
    const [currency, setCurrency] = useState('USD')


    async function getSelectedCars() {
        const response = await axios.get("http://127.0.0.1:8000/cars/" + location.state.selectedMark + "/")
        setSelectedCars(response.data)
    }

    useEffect(() => {
        getSelectedCars()}, [])

    const handleCarsCount = (carsCount) => {
        setCarsCount(carsCount)
        }

    const handleChangeMark = (markLink) => {
        setMarkLink(markLink)
        setSelectedCars(cars.filter(car => car.mark_link === markLink))

  }

   const handleChangeModel = (modelLink) => {
        setModelLink(modelLink)
        setSelectedCars(cars.filter(car => car.model_link === modelLink))
    }

    const handleChangeYearFrom = (year) => {
        setYearFrom(Number(year))
         if (markLink !== "" && modelLink !== "" && yearTo !== null) {
             setSelectedCars(cars.filter(car => car.model_link === modelLink && car.mark_link === markLink && car.year >= year && car.year <= yearTo))
             }else if(markLink !== "" && modelLink === "" && yearTo !== null){
                 setSelectedCars(cars.filter(car => car.mark_link === markLink && car.year >= year && car.year <= yearTo))
             }else if(markLink === "" && modelLink === "" && yearTo === null){
                 setSelectedCars(cars.filter(car => car.year >= year))
             }else if(markLink === "" && modelLink === "" && yearTo !== null){
                 setSelectedCars(cars.filter(car => car.year >= year && car.year <= yearTo))
             }else if(markLink !== "" && modelLink !== "" && yearTo === null){
                 setSelectedCars(cars.filter(car => car.model_link === modelLink && car.mark_link === markLink && car.year >= year))
             }else if (markLink !== "" && modelLink === "" && yearTo === null){
                 setSelectedCars(cars.filter(car => car.mark_link === markLink && car.year >= year))
                 }
    }

    const handleChangeYearTo = (year) => {
        setYearTo(Number(year))
        if (markLink !== "" && modelLink !== "" && yearFrom !== null) {
             setSelectedCars(cars.filter(car => car.model_link === modelLink && car.mark_link === markLink && car.year >= yearFrom && car.year <= year))
             }else if (markLink !== "" && modelLink !== "" && yearFrom === null){
                 setSelectedCars(cars.filter(car => car.model_link === modelLink && car.mark_link === markLink && car.year <= year))
             }else if (markLink !== "" && modelLink === "" && yearFrom !== null){
                 setSelectedCars(cars.filter(car => car.mark_link === markLink && car.year >= yearFrom && car.year <= year))
             }else if (markLink === "" && yearFrom === null){
                 setSelectedCars(cars.filter(car => car.year <= year))
             }else if (markLink === "" && yearFrom !== null){
                 setSelectedCars(cars.filter(car => car.year >= yearFrom && car.year <= year))
             }else if (markLink !== "" && modelLink === "" && yearFrom === null){
                 setSelectedCars(cars.filter(car => car.mark_link === markLink && car.year <= year))
                 }
             }

   const handlePriceFrom = (price) => {
         setPriceFrom(price)
        }

    const handlePriceTo = (price) => {
        setPriceTo(price)
        }

    const handleCurrency = (currency) => {
        setCurrency(currency)
         }

    const searchForPrice = (event) => {
        if((markLink !== '' || modelLink !== '' || yearFrom !== null || yearTo !== null)&& currency === "USD"){
            setSelectedCars(selectedCars.filter(car => car.card_price_secondary >= priceFrom && car.card_price_secondary <= priceTo))
        }else if((markLink !== '' || modelLink !== '' || yearFrom !== null || yearTo !== null)&& currency === "BYN"){
             setSelectedCars(selectedCars.filter(car => car.card_price_primary >= priceFrom && car.card_price_primary <= priceTo))
        }else if((markLink === '' || modelLink === '' || yearFrom === null || yearTo === null)&& currency === "BYN"){
             setSelectedCars(cars.filter(car => car.card_price_primary >= priceFrom && car.card_price_primary <= priceTo))
        }else if((markLink === '' || modelLink === '' || yearFrom === null || yearTo === null)&& currency === "USD"){
             setSelectedCars(cars.filter(car => car.card_price_secondary >= priceFrom && car.card_price_secondary <= priceTo))
        }
    }

    const reset = (event) => {
        setMarkLink('')
        setModelLink('')
        setYearFrom(null)
        setYearTo(null)
        setPriceFrom(0)
        setPriceTo(10000000)
        setCurrency('USD')
        setSelectedCars([])
        }


    if (location.state.count===0) {
        return(
            <div>
            <img className="general-pic" src={general_pic} alt="fish"/>
                <GeneralLineTable/>
            <h3> Нет доступных моделей </h3>
            </div>
        )
    }

    return(
        <div>
            <img className="general-pic" src={general_pic} alt="fish"/>
            <GeneralLineTable/>
            <FindForParamsForm changedPriceFrom={handlePriceFrom} changedPriceTo={handlePriceTo}
                               changedCurrency={handleCurrency} searchForPrice={searchForPrice}
                               changedYearFrom={handleChangeYearFrom} changedYearTo={handleChangeYearTo}
                               changedModelLink={handleChangeModel} changedMarkLink={handleChangeMark}
                               changedCarsCount={handleCarsCount} carsCount={carsCount} defaultCount={location.state.count}
                               defaultValue={mark} defaultValueId={location.state.id} models={models}
                               generalItems={generalItems} cars={cars} reset={reset}/>
            <div></div>
            <div>My link is:{markLink}</div>
            <div>My count is:{location.state.count}</div>
            <div>My count is:{location.state.id}</div>
            <div>My id is:{cars.mark_link}</div>
            <tr class="tr-car-item">
                 <CarsTable carsCount={selectedCars.length} cars={selectedCars}/>
            </tr>

            </div>


        )}


export default SelectedCarMarkPage;