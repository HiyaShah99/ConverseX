// import Testimonials from "./sections/Testimonials";
// import Footer from "./sections/Footer";
// import Contact from "./sections/Contact";
// import TechStack from "./sections/TechStack";
// import Experience from "./sections/Experience";
// import Hero from "./sections/Hero";
// import ShowcaseSection from "./sections/ShowcaseSection";
// import LogoShowcase from "./sections/LogoShowcase";
// import FeatureCards from "./sections/FeatureCards";
// import Navbar from "./components/NavBar";

// const App = () => (
//   <>
//     <Navbar />
//     <Hero />
//     <ShowcaseSection />
//     <LogoShowcase />
//     <FeatureCards />
//     <Experience />
//     <TechStack />
//     <Testimonials />
//     <Contact />
//     <Footer />
//   </>
// );

// export default App;

import {
  BrowserRouter as Router,
  Routes,
  Route,
  useNavigate
} from "react-router-dom";

import Navbar from "./components/NavBar";
import Hero from "./sections/Hero";
import ShowcaseSection from "./sections/ShowcaseSection";
import LogoShowcase from "./sections/LogoShowcase";
import FeatureCards from "./sections/FeatureCards";
import Experience from "./sections/Experience";
import TechStack from "./sections/TechStack";
import Testimonials from "./sections/Testimonials";
import Contact from "./sections/Contact";
import Footer from "./sections/Footer";

const FullPage = () => (
  <>
    <Hero />
    {/* <ShowcaseSection /> */}
    {/* <LogoShowcase /> */}
    {/* <FeatureCards /> */}
    {/* <Experience /> */}
    {/* <TechStack /> */}
    {/* <Testimonials /> */}
    {/* <Contact /> */}
    <Footer />
  </>
);

const WorkPage = () => (
  <div style={{ padding: "2rem", fontSize: "1.5rem" }}>
    <h1>This is the MEET (Work) Page!</h1>
  </div>
);

const App = () => (
  <Router>
    <Navbar />
    <Routes>
      <Route path="/" element={<FullPage />} />
      <Route path="/work" element={<WorkPage />} />
    </Routes>
  </Router>
);

export default App;
