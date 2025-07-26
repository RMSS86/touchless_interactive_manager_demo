export async function useLocalUser({
  _user,
  _userDispatcher,
  _storageKey,
  _storage = "",
  _action,
}: _globalUserProps) {
  //////VERIFICATION ON LOCAL STORAGE//////VERIFICATION ON LOCAL STORAGE////
  //////VERIFICATION ON LOCAL STORAGE//////VERIFICATION ON LOCAL STORAGE////
  if (_action === "verify") {
    const _noStorage = window.localStorage.getItem("user") === null;
    const _rawUser = _user?._active === false;

    if (_noStorage && _rawUser) {
      return; //< false && false
    }
    if (_noStorage === false && _rawUser === true) {
      const _locallyStoredData = await JSON.parse(
        localStorage.getItem("user")!
      ); //< localStorage Only
      _userDispatcher!(_locallyStoredData); //< make it global
      console.log("FROM useLocalUser Hook: ", _locallyStoredData);
      return;
    }
  }
  //////VERIFICATION ON LOCAL STORAGE//////VERIFICATION ON LOCAL STORAGE////
  //////SAVE TO LOCAL STORAGE//////SAVE TO LOCAL STORAGE//////SAVE TO LOCAL STORAGE//////
  if (_action === "store") {
    localStorage.setItem(_storageKey!, _storage!)!;
    const _toGetStoredData = await JSON.parse(
      localStorage.getItem(_storageKey!)!
    );
    console.log("from store hook! ", _toGetStoredData);
    _userDispatcher!(_toGetStoredData);
  }
  //////SAVE TO LOCAL STORAGE//////SAVE TO LOCAL STORAGE//////SAVE TO LOCAL STORAGE//////
  //////REMOVE TO LOCAL STORAGE//////SAVE TO LOCAL STORAGE//////SAVE TO LOCAL STORAGE//////
  if (_action === "remove") {
    localStorage.removeItem(_storageKey!);
  }
  //////REMOVE TO LOCAL STORAGE//////SAVE TO LOCAL STORAGE//////SAVE TO LOCAL STORAGE//////
}

type _globalUserProps = {
  _user?: User | null;
  _storage?: string;
  _userDispatcher?: React.Dispatch<React.SetStateAction<User | null>>;
  _storageKey?: string;
  _action?: "store" | "remove" | "verify";
};
import { User } from "../types/userType";
