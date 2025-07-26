export const hideAlert = () => {
  const element = document.querySelector(".alert");
  if (element) element.parentElement.removeChild(element);
};

// type is 'success' or 'error'
export const showAlert = (type, msg, delay = 5000) => {
  hideAlert();
  const markup = `<div class="alert alert-${type}">${msg}</div>`;
  document.querySelector("body").insertAdjacentHTML("afterbegin", markup);
  window.setTimeout(hideAlert, delay);
};

import "./alerts.scss";
