const HEADER_DATA: _menuFeature[] = [
  { id: 0, menu: "Home", direct: "/" },
  { id: 1, menu: "Schedule", direct: "schedule" },
  { id: 2, menu: "Exceptions", direct: "exceptions" },
  { id: 3, menu: "User", direct: "user" },
];

const FOOTER_DATA: footerTag[] = [
  { tag: "About", link: "about" },
  { tag: "Stories", link: "#" },
  { tag: "Tutorials", link: "www.udemy.com" },
  { tag: "Careers", link: "www." },
  { tag: "Blog", link: "www.medium.com" },
  { tag: "Contact us", link: "https://www.linkedin.com/in/robert-solis-stevenson-6a458a265/" },
];

//HOMEPAGE
const HOMEPAGE_DATA: _heading_text[] = [
  {id: 1, tag: 'Landing_title', text: 'Interactive Touchless Manager' },
  {id: 2, tag: 'Landing_paragraph', text: 'This product is designed for a new era where the conditions about entering in contact with the incorrect person could be critical, this system integrates Computer vision and Machine Learning models for assistance porpuses.' },


]

const BRAND_NAME: string = 'TIM'

  var ASSETS_LOCATIONS: location[] = [
    { id: 1, name: "HeadQuarters ", position: [14.579503, -90.495271] },
    { id: 2, name: "Store #1 ", position: [14.6262056, -90.5749618] },
    { id: 3, name: "Store #2 ", position: [14.5727815,-90.5384374] },
  ];

  type location = {
    id: number;
    name: string;
    position: PointTuple;
    assets?: '';
  };
   type _heading_text = {
    id: number;
    tag: string;
    text: string;

   };
export { HEADER_DATA, FOOTER_DATA ,ASSETS_LOCATIONS ,BRAND_NAME, HOMEPAGE_DATA};  
// export { LOCAIION_TILE_ITEMS,SUB_HEADER_ITEMS }; 

/////TYPES/////TYPES/////TYPES/////TYPES/////TYPES/////TYPES/////TYPES////
/////TYPES/////TYPES/////TYPES/////TYPES/////TYPES/////TYPES/////TYPES////
type _icons = {
  icon: string;
}

type _menuFeature = {
  id: number;
  menu: string;
  direct: string;
  action?: () => void;
};

type footerTag = {
  tag: string;
  link: string;
  _function?: () => {};
};

type _brandings = {
  logoName: string;
  logoDir: string;
  direct: string;
  alt: string;
};

import { PointTuple } from 'leaflet';
// import {
//     Add_circle_icon,     
//     delete_icon,
//     search_icon,
//     Fav_icon,
//     Qr_scan_icon, //@ts-ignore
//   } from '../../assetsImport.js';


// const SUB_HEADER_ITEMS: _icons[] = [
//   { icon: Add_circle_icon },
//   { icon: delete_icon },
//   { icon: Fav_icon },
//   { icon: search_icon },
//   { icon: Qr_scan_icon },

// ]
// const LOCAIION_TILE_ITEMS: _icons[] = [
//   { icon: Add_circle_icon },
//   { icon: Qr_scan_icon },
//   { icon: delete_icon },

// ]