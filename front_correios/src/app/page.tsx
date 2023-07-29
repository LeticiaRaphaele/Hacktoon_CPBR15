import { cva } from 'class-variance-authority'
import Head from 'next/head';
import Navbar from './components/Navbar';
import Box from './components/box';

const container = cva(['flex bg-yellow mt-30']);
export default function Home() {
  return (
    
    <div className={container()}>
      
      <Head>Correios</Head> 
      <Box></Box>
      
      </div>
  );
 
}
