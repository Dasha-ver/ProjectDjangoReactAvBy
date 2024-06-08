import React, {useState} from "react" ;
import general_pic from "./pictures/general-pic.jpg";
import FindForParamsForm from "./FindForParamsForm"
import GeneralPageItemsTable from "./GeneralPageItemsTable"
import SecondAd from "./SecondAd"
import GeneralLineTable from "./GeneralLineTable"
import CarsTable from "./CarsTable"


const GeneralPage= ({generalItems, cars, models}) => {

    const [selectedCars, setSelectedCars] = useState([])
    const [carsCount, setCarsCount] = useState('')
    const [mark, setMark] = useState('')
    const [model, setModel] = useState('')
    const [yearFrom, setYearFrom] = useState(null)
    const [yearTo, setYearTo] = useState(null)
    const [priceFrom, setPriceFrom] = useState(0)
    const [priceTo, setPriceTo] = useState(10000000)
    const [currency, setCurrency] = useState('USD')


    const handleMarkCount = (markCount) => {
        setCarsCount(markCount)
    }

    const handleChangeMark = (markLink) => {
        setMark(markLink)
        setSelectedCars(cars.filter(car => car.mark_link === markLink))
    }

    const handleChangeModel = (modelLink) => {
        setModel(modelLink)
        setSelectedCars(cars.filter(car => car.model_link === modelLink))
    }


    const handleChangeYearFrom = (year) => {
        setYearFrom(Number(year))
         if (mark !== "" && model !== "" && yearTo !== null) {
             setSelectedCars(cars.filter(car => car.model_link === model && car.mark_link === mark && car.year >= year && car.year <= yearTo))
             }else if(mark !== "" && model === "" && yearTo !== null){
                 setSelectedCars(cars.filter(car => car.mark_link === mark && car.year >= year && car.year <= yearTo))
             }else if(mark === "" && model === "" && yearTo === null){
                 setSelectedCars(cars.filter(car => car.year >= year))
             }else if(mark === "" && model === "" && yearTo !== null){
                 setSelectedCars(cars.filter(car => car.year >= year && car.year <= yearTo))
             }else if(mark !== "" && model !== "" && yearTo === null){
                 setSelectedCars(cars.filter(car => car.model_link === model && car.mark_link === mark && car.year >= year))
             }else if (mark !== "" && model === "" && yearTo === null){
                 setSelectedCars(cars.filter(car => car.mark_link === mark && car.year >= year))
    }
}

    const handleChangeYearTo = (year) => {
        setYearTo(Number(year))
        if (mark !== "" && model !== "" && yearFrom !== null) {
             setSelectedCars(cars.filter(car => car.model_link === model && car.mark_link === mark && car.year >= yearFrom && car.year <= year))
             }else if (mark !== "" && model !== "" && yearFrom === null){
                 setSelectedCars(cars.filter(car => car.model_link === model && car.mark_link === mark && car.year <= year))
             }else if (mark !== "" && model === "" && yearFrom !== null){
                 setSelectedCars(cars.filter(car => car.mark_link === mark && car.year >= yearFrom && car.year <= year))
             }else if (mark === "" && yearFrom === null){
                 setSelectedCars(cars.filter(car => car.year <= year))
             }else if (mark === "" && yearFrom !== null){
                 setSelectedCars(cars.filter(car => car.year >= yearFrom && car.year <= year))
             }else if (mark !== "" && model === "" && yearFrom === null){
                 setSelectedCars(cars.filter(car => car.mark_link === mark && car.year <= year))
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
        if((mark !== '' || model !== '' || yearFrom !== null || yearTo !== null)&& currency === "USD"){
            setSelectedCars(selectedCars.filter(car => car.card_price_secondary >= priceFrom && car.card_price_secondary <= priceTo))
        }else if((mark !== '' || model !== '' || yearFrom !== null || yearTo !== null)&& currency === "BYN"){
             setSelectedCars(selectedCars.filter(car => car.card_price_primary >= priceFrom && car.card_price_primary <= priceTo))
        }else if((mark === '' || model === '' || yearFrom === null || yearTo === null)&& currency === "BYN"){
             setSelectedCars(cars.filter(car => car.card_price_primary >= priceFrom && car.card_price_primary <= priceTo))
        }else if((mark === '' || model === '' || yearFrom === null || yearTo === null)&& currency === "USD"){
             setSelectedCars(cars.filter(car => car.card_price_secondary >= priceFrom && car.card_price_secondary <= priceTo))
        }
    }

    const reset = (event) => {
        setMark('')
        setModel('')
        setYearFrom(null)
        setYearTo(null)
        setPriceFrom(0)
        setPriceTo(10000000)
        setCurrency('USD')
        setSelectedCars([])
        }

    if (!generalItems.length) {
        return <h3> Нет информации </h3>
    }

    return(

         <div>
          <img className="general-pic" src={general_pic} alt="fish"/>
            <GeneralLineTable/>
            <SecondAd/>
            <GeneralPageItemsTable generalItems={generalItems} cars={cars}/>
            <FindForParamsForm changedPriceFrom={handlePriceFrom} changedPriceTo={handlePriceTo}
                               changedCurrency={handleCurrency} searchForPrice={searchForPrice}
                               changedYearFrom={handleChangeYearFrom} changedYearTo={handleChangeYearTo}
                               changedModelLink={handleChangeModel} changedMarkLink={handleChangeMark}
                               changedMarkCount={handleMarkCount} carsCount={carsCount} generalItems={generalItems}
                               models={models} cars={cars} reset={reset}/>
            <div>{mark}, {yearFrom}, {priceFrom}, {currency}</div>
            <CarsTable carsCount={carsCount} cars={selectedCars}/>
         </div>
    )
}

export default GeneralPage;


