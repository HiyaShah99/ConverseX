import { useRef } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useGSAP } from "@gsap/react";

gsap.registerPlugin(ScrollTrigger);

const AppShowcase = () => {
  const sectionRef = useRef(null);
  const rydeRef = useRef(null);
  const libraryRef = useRef(null);
  const ycDirectoryRef = useRef(null);

  useGSAP(() => {
    // Animation for the main section
    gsap.fromTo(
      sectionRef.current,
      { opacity: 0 },
      { opacity: 1, duration: 1.5 }
    );

    // Animations for each app showcase
    const cards = [rydeRef.current, libraryRef.current, ycDirectoryRef.current];

    cards.forEach((card, index) => {
      gsap.fromTo(
        card,
        {
          y: 50,
          opacity: 0,
        },
        {
          y: 0,
          opacity: 1,
          duration: 1,
          delay: 0.3 * (index + 1),
          scrollTrigger: {
            trigger: card,
            start: "top bottom-=100",
          },
        }
      );
    });
  }, []);

  return (
    <div id="work" ref={sectionRef} className="app-showcase">
      <div className="w-full">
        <div className="showcaselayout">
          <div ref={rydeRef} className="first-project-wrapper">
            <div className="image-wrapper">
              <img src="/images/project1.png" alt="Ryde App Interface" />
            </div>
            <div className="text-content">
              <h2>
                On-Demand Rides Made Simple with a Powerful, User-Friendly App
                called Ryde
              </h2>
              <p className="text-white-50 md:text-xl">
                An app built with React Native, Expo, & TailwindCSS for a fast,
                user-friendly experience.
              </p>
            </div>
          </div>

          <div className="project-list-wrapper overflow-hidden">
            <div className="project" ref={libraryRef}>
              <div className="image-wrapper bg-[#FFEFDB]">
                <img
                  src="/images/project2.png"
                  alt="Library Management Platform"
                />
              </div>
              <h2>The Library Management Platform</h2>
            </div>

            <div className="project" ref={ycDirectoryRef}>
              <div className="image-wrapper bg-[#FFE7EB]">
                <img src="/images/project3.png" alt="YC Directory App" />
              </div>
              <h2>YC Directory - A Startup Showcase App</h2>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AppShowcase;
// import { useEffect, useRef, useState } from "react";
// import { Canvas, useFrame } from "@react-three/fiber";
// import { OrbitControls } from "@react-three/drei";
// import { Html } from "@react-three/drei";

// import * as THREE from "three";
// import { io } from "socket.io-client";

// const socket = io("http://localhost:3000"); // match with your server port

// const BUBBLE_RADIUS = 1;
// const INTERACTION_DISTANCE = 3;

// const Bubble = ({ id, position, username, isSpeaking }) => {
//   const meshRef = useRef();

//   useFrame(() => {
//     if (meshRef.current) {
//       // Float slightly
//       meshRef.current.position.y += 0.005 * Math.sin(Date.now() / 300);
//     }
//   });

//   return (
//     <mesh position={position} ref={meshRef}>
//       <sphereGeometry args={[BUBBLE_RADIUS, 32, 32]} />
//       <meshStandardMaterial color={isSpeaking ? "orange" : "skyblue"} />
//       <Html>
//         <div style={{ color: "white", textAlign: "center" }}>{username}</div>
//       </Html>
//     </mesh>
//   );
// };

// const ShowcaseSection = () => {
//   const [bubbles, setBubbles] = useState([]);

//   useEffect(() => {
//     socket.on("users", (users) => {
//       setBubbles(users);
//     });

//     // New user joins
//     const username = "User" + Math.floor(Math.random() * 1000);
//     socket.emit("join", { username });

//     return () => socket.disconnect();
//   }, []);

//   return (
//     <div style={{ height: "100vh" }}>
//       <section id="meet" style={{ height: '100vh' }}>
//   <Canvas camera={{ position: [0, 0, 10], fov: 50 }}>
//     <ambientLight intensity={0.5} />
//     <OrbitControls />
//     <pointLight position={[10, 10, 10]} />
//     {bubbles.map((user) => (
//           <Bubble
//             key={user.id}
//             id={user.id}
//             username={user.username}
//             position={user.position}
//             isSpeaking={user.isSpeaking}
//           />
//         ))}
//   </Canvas>
//       </section>
//     </div>


//   );
// };

// export default ShowcaseSection;
