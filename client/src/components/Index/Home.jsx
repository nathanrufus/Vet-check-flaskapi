import React, { useEffect, useState } from 'react'
import image from '../Assets/scre2.jpg'
import './Home.css'

function Home() {
const[term ,setterm]=useState([])
useEffect(()=>{
fetch('http://127.0.0.1:5000/owners')
  .then(resp=>resp.json())
  .then(data=>setterm(data))
},[])

  return (
    <div>
        <section className="myhome">
          {term.map((obj)=>(
            <div className="content" key={obj.id}>
                <img src={image}alt="my image" />
                <h1>my name is {obj.username}</h1>
                <span className="email">contact me in :{obj.email} </span>
            </div>
          ))}
        </section>
        </div>
  )
}

export default Home