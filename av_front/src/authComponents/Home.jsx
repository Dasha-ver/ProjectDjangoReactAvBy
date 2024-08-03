import React from 'react'
import { useEffect,useState } from 'react'
import axios from 'axios'


const Home = () => {
  const [username, setUsername] = useState('');
  const [userId, setUserId] = useState('');

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
  },[]);
  return (
    <div className="form-signin mt-5 text-center">
    <h3>Добро пожаловать, {username}!</h3>
    <div>{userId}</div>
  </div>
  )
}

export default Home