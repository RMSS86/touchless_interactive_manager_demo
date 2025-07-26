const _menuFeatures: _menuFeatures[] = [
  { menu: "Home", href: "" },
  { menu: "Tours", href: "tours" },
  { menu: "Trending", href: "top-tours" },
  { menu: "Discover", href: "booking" },
];
type _menuFeatures = {
  menu: string;
  href: string;
  action?: () => void;
};
const noNAVS: NAV[] = [
  {
    logo: "",
    navIndex: "01",
    nav: "About Trax",
    href: "/",
  },
  {
    logo: "",
    navIndex: "02",
    nav: "logIn",
    href: "login",
  },
  {
    logo: "",
    navIndex: "03",
    nav: "Tours",
    href: "tours",
  },
  {
    logo: "",
    navIndex: "06",
    nav: "Contact Us",
    href: "",
  },
];

const NAVS: NAV[] = [
  {
    logo: "",
    navIndex: "01",
    nav: "Home",
    href: "",
  },
  {
    logo: "",
    navIndex: "02",
    nav: "Account",
    href: "profile",
  },
  {
    logo: "",
    navIndex: "03",
    nav: "Tours",
    href: "tours",
  },
  {
    logo: "",
    navIndex: "04",
    nav: "Trending",
    href: "",
  },
  {
    logo: "",
    navIndex: "05",
    nav: "Bookings",
    href: "",
    // function: () => this.NAV.nav,
  },
  {
    logo: "",
    navIndex: "06",
    nav: "Contact Us",
    href: "",
  },
];

//export
type NAV = {
  logo: string;
  navIndex: string;
  nav: string;
  href: string;
  function?: () => void;
};

type UserSideMenu = {
  _link: string;
  _text: string;
  _icon: string;
  _active: boolean;
};

const _email: Email = {
  email: "",
};
const _userDefault: User = {
  _id: "",
  _role: "user",
  _active: false,
  _name: "",
  _email: "",
  _passwordChangedAt: "",
  _token: "",
  _imgDir: "",
  _photo: "",
  _img: "",
};

const _loginDefault: Login = {
  email: "",
  password: "",
};
const _passwordUpdate: PasswordUpdate = {
  passwordCurrent: "",
  password: "",
  passwordConfirm: "",
};
const _userUpdateDefault: UpdateUser = {
  name: "",
  email: "",
  photo: undefined,
};
/////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
/////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
import {
  User,
  Login,
  PasswordReset,
  PasswordUpdate,
  UpdateUser,
  Email, //@ts-ignore
} from "../../models/types/userType";

//////EXPORTS//////EXPORTS//////EXPORTS//////EXPORTS//////EXPORTS//////EXPORTS/////////
//////EXPORTS//////EXPORTS//////EXPORTS//////EXPORTS//////EXPORTS//////EXPORTS/////////
export {
  _menuFeatures,
  NAVS,
  noNAVS,
  _userDefault,
  _loginDefault,
  _passwordUpdate,
  _userUpdateDefault,
  _email,
};
export type { NAV, UserSideMenu, User };
