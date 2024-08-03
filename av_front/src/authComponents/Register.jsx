import React,{useState} from 'react'
import axios from 'axios'
import validator from 'validator'

const Register = () => {
  const [username,setUsername] = useState('');
  const [password,setPassword] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('')
  const [emailError, setEmailError] = useState('')

  const submit = async e =>{

    e.preventDefault()
    if (validator.isEmail(username) && repeatPassword === password){

        const user = {
          username:username,
          password:password
        };



        await fetch(' http://127.0.0.1:8000/register/',{
          method:'POST',
          headers:{'Content-Type':"application/json"},
          body: JSON.stringify(
            {
              username,
              password
            }
          )
        });
        window.location.href='/login'
}else{
    setEmailError('Enter valid Email!')
    }
  }

  return (
    <div className="Auth-form-container">
    <form className="Auth-form" onSubmit={submit}>
      <div className="Auth-form-content">
        <h3 className="Auth-form-title">Регистрация</h3>
        <div className="form-group mt-3">
          <label class="input-label">E-mail</label>
          <input className="form-control mt-1"
            placeholder="Enter e-mail"
            name='username'
            type='text'
            value={username}
            required
            onChange={e => setUsername(e.target.value)}/>
        </div>
        <div className="form-group mt-3">
          <label class="input-label">Пароль</label>
          <input
            name='password'
            type="password"
            className="form-control mt-1"
            placeholder="Enter password"
            value={password}
            required
            onChange={e => setPassword(e.target.value)}/>
        </div>
        <div className="form-group mt-3">
          <label class="input-label">Подтвердите пароль</label>
          <input
            name='repeatPassword'
            type="password"
            className="form-control mt-1"
            placeholder="Repeat password"
            value={repeatPassword}
            required
            onChange={e => setRepeatPassword(e.target.value)}/>
        </div>
        <span style={{
          fontWeight: 'bold',
          color: 'red',
        }}>{emailError}</span>
        <div className="d-grid gap-2 mt-3">
          <button type="submit"
             className="btn btn-primary">Подтвердить</button>
        </div>
      </div>
   </form>
 </div>
  )
}

export default Register