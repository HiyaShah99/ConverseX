import { socialImgs } from "../constants";

const Footer = () => {
  return (
    <footer className="footer bg-white-50 dark:bg-black-50 text-black-100 dark:text-white-100 p-6 ">
      <div className="footer-container">
        <div className="flex flex-col justify-center">
          {/* <p>Terms & Conditions</p> */}
        </div>
        <div className="socials">
          {/* {socialImgs.map((socialImg, index) => (
            <div key={index} className="icon">
              <img src={socialImg.imgPath} alt="social icon" />
            </div>
          ))} */}

        </div>
        <div className="flex flex-col justify-center">
          <p className="text-center md:text-end text-white">
            {/* © {new Date().getFullYear()} Adrian Hajdin. All rights reserved. */}
            © ConverseX
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
