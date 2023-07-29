import { cva } from 'class-variance-authority'
import Head from 'next/head';

const container = cva(['flex bg-yellow w-full']);
const MainMenu = cva(['inline-flex bg-violet-900 h-30 w-full'])
export default function Navbar() {
  return (
    
    <div className={container()}><nav className={MainMenu()}>
            <a href='#'>menu</a>
        </nav>
        
    </div>
  );
 
}