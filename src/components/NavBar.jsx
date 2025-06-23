import { useState, useEffect } from "react";
import { navLinks } from "../constants";

const NavBar = () => {
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      const isScrolled = window.scrollY > 10;
      setScrolled(isScrolled);
    };

    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  // ✅ Miro Sticky Note Function
  const handleCreateStickyNote = async () => {
    if (!window.miro || !window.miro.board) {
      alert("Please open this app inside a Miro board.");
      return;
    }

    try {
      await window.miro.board.widgets.create({
        type: 'sticky_note',
        text: 'Hello from ConverseX!',
        x: 0,
        y: 0,
        style: {
          fillColor: 'light_yellow',
        },
      });
    } catch (error) {
      console.error('Miro error:', error);
    }
  };

  return (
    <header className={`navbar ${scrolled ? "scrolled" : "not-scrolled"}`}>
      <div className="inner">
        <a href="#hero" className="logo border-b-2 border-white-100 text-white-100">
          CONVERSEX
        </a>

        <nav className="desktop">
          <ul className="flex space-x-8">
            {[
              {
                label: 'Meet',
                href: 'https://preview--glow-bubble-chat-verse.lovable.app/',
              },
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

            {/* ✅ Miro Button */}
            <li className="group relative cursor-pointer">
              <button
                onClick={handleCreateStickyNote}
                className="transition-colors duration-300 group-hover:text-white text-[20px]"
              >
                Add Sticky Note
              </button>
              <span className="absolute -bottom-1 left-0 h-0.5 w-0 bg-white transition-all duration-300 group-hover:w-full"></span>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default NavBar;
