import React, {useState} from "react";
import Dropdown from "react-bootstrap/Dropdown";
import GeneralItemMark from "./GeneralItemMark"
import Form from 'react-bootstrap/Form';


const ScrollableDropdownGeneralItems = ({generalItems}) =>{

    const[mark, setMark] = useState(null);
    const[value, setValue] = useState('')
    const filteredGeneralItems = generalItems.filter(generalItem => {
        return generalItem.title.toLowerCase().includes(value.toLowerCase())
    })

    return (

        <Dropdown>
             <Dropdown.Toggle
                 variant="white"
                 placeholder="Select Country"
                >
                  Марка
             </Dropdown.Toggle>

             <Dropdown.Menu
                 style={{
                     maxHeight: "200px",
                     overflowY: "auto",
                 }}>

                 <Form.Control
                      autoFocus
                      className="mx-3 my-2 w-auto"
                      placeholder="Поиск"
                      onChange={(e) => setValue(e.target.value)}
                      value={value}
                    />
                 <Dropdown.Item href="#">Любой</Dropdown.Item>
                 <Dropdown.Item href="#"><div>{ filteredGeneralItems.sort((a, b) =>
                                                a.title.localeCompare(b.title)).map(generalItemMark =>
                                                <GeneralItemMark generalItemMark={generalItemMark} key={generalItemMark.id}/>)}
                                         </div>


             </Dropdown.Item>

             </Dropdown.Menu>
         </Dropdown>
    );
};


export default ScrollableDropdownGeneralItems;

