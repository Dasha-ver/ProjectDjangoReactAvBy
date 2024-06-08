import React, {useState} from "react";
import {useNavigate} from 'react-router-dom';
import SelectedCarMarkPage from "./SelectedCarMarkPage"

const GeneralItem = (props) => {

    const navigate = useNavigate();


    return(
         <tr>
             <td>
                <button onClick={() => navigate("/SelectedCar",{state:{link:props.generalItem.link, count:props.generalItem.count, selectedMark:props.generalItem.title, id: props.generalItem.id}})} class="btn-general-page-item" ><td class="td-general-page-item-mark" >{props.generalItem.title}</td>
             <td class="td-general-page-item-mark-count">{props.generalItem.count}</td></button></td>
         </tr>
    )











}

export default GeneralItem;






