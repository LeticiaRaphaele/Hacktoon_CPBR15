'use client'
import { cva } from 'class-variance-authority'
import Head from 'next/head';
import axios from 'axios';
import { useState, useEffect } from 'react';

const container = cva(['flex-col bg-yellow w-full ']);
const MainMenu = cva(['inline-flex bg-violet-900 h-30 w-full'])
export default function Bairro() {
    const [city, setCity] = useState<any[]>([])
    useEffect(()=>{
       fetchCities();
    },[])
   function fetchCities(){
    axios.get('http://localhost:5000/bairros').then((res)=>{
        console.log(res.data);
        setCity(res.data);
}).catch(()=>{
    console.log("erro")
})
   }

  return (
    
    <div className={container()}>
        <br/>
        <h1 className='text-5xl mb-30'>Cidades </h1> <br/>
        {city.map((data):any=>(
            
            <div >
               
                <p key={data.id} className='gap-2'><span>CEP: {data.CEP}</span> <br/>
                 <span className='mr-2'>ID_Bairro: {data.ID_Bairro}</span><br/>
                  <span>NomeBairro: {data.NomeBairro}</span><br/>
                    <span>Regiao: {data.Regiao}</span> </p><br/>
                </div>
        ))}
    </div>
  );
 
}