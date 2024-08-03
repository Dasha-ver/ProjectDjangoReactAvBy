import React, { useState, useEffect} from 'react';
import {Link} from 'react-router-dom'

const Navigate = () => {
	const [isAuth,setIsAuth] = useState(false)
	useEffect(() => {
		if(localStorage.getItem('access_token') !== null){
			setIsAuth(true);
		}
	},[isAuth]);

    return (

          <>
          <nav class="navbar navbar-expand-lg bg-body-tertiary">
          <div class="container-fluid">
            <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
              <ul class="navbar-nav me-auto mb-2 mb-lg-0">

                {isAuth ? <Link to="/" className='nav-link active'>Личный кабинет</Link> : null}
                {isAuth ? <Link to="/logout" className='nav-link active'>Выйти</Link> :

                          <Link to="/login" className='nav-link active'>Войти</Link>}
                {isAuth ? " ":

                           <Link to="/register" className='nav-link active'>Регистрация</Link>}
              </ul>

            </div>
          </div>
        </nav>
          </>
          )
}

export default Navigate


