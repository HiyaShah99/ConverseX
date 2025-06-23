import { useState, useEffect } from "react";

import { navLinks } from "../constants";

const NavBar = () => {
  // track if the user has scrolled down the page
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    // create an event listener for when the user scrolls
    const handleScroll = () => {
      // check if the user has scrolled down at least 10px
      // if so, set the state to true
      const isScrolled = window.scrollY > 10;
      setScrolled(isScrolled);
    };

    // add the event listener to the window
    window.addEventListener("scroll", handleScroll);

    // cleanup the event listener when the component is unmounted
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <header className={`navbar ${scrolled ? "scrolled" : "not-scrolled"}`}>
      <div className="inner">
        <a href="#hero" className="logo border-b-2 border-white-100 text-white-100">
          CONVERSEX
        </a>

        <nav className="desktop">
        <ul className="flex space-x-8">
          {[
            { label: 'Meet', href: 'https://preview--glow-bubble-chat-verse.lovable.app/' },
            // { label: 'Experience', href: '#' },
            // { label: 'Connect', href: '#' },
            // { label: 'Feedback', href: '#' },
          ].map((item, idx) => (
            <li key={idx} className="group relative cursor-pointer">
              <a
                href={item.href}
                target="_blank"
                rel="noopener noreferrer"
                className="transition-colors duration-300 group-hover:text-white text-[20px]"
              >
                {item.label}
              </a>
              <span className="absolute -bottom-1 left-0 h-0.5 w-0 bg-white transition-all duration-300 group-hover:w-full"></span>
            </li>
          ))}
        </ul>

  
</nav>
        
      </div>
    </header>
  );
}

export default NavBar;
