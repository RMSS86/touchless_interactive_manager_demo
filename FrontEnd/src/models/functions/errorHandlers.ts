/////FUNCTIONS/////FUNCTIONS/////FUNCTIONS/////FUNCTIONS/////FUNCTIONS////
/////FUNCTIONS/////FUNCTIONS/////FUNCTIONS/////FUNCTIONS/////FUNCTIONS////

//////GENERAL ERROR HANDLER////GENERAL ERROR HANDLER////
export async function httpErrorGenerator(_err: Response) {
  try {
    let errorStatusCode;
    let errorMessage;

    // errorClassifier(_err);
    const _errData = await _err.json();
    errorStatusCode = _errData.error.statusCode;
    errorMessage = _errData.message;

    // console.log(_errData);
    console.log(errorStatusCode);
    console.log(errorMessage);
    // return { errorStatusCode, errorMessage };

    showAlert(
      "error",
      `Something Went Wrong!\nStatusCode: [ ${errorStatusCode} ]\n${errorMessage} `
    );
  } catch (_error) {
    console.log(_error);
    showAlert("error", `Something Went Wrong!\nError: [ ${_error} ]\n`);
  }

  // throw new Response(JSON.stringify({ message: errorMessage }), {
  //   status: errorStatusCode,
  //   statusText: "HTTP-FAIL",
  // });
}

export function errorClassifier(_err: Response) {
  /////// claication?
  // console.log("from error clasifyer ", _err);
  // console.log("from error clasifyer ", _err.statusText);
  // if (_err === "") throw new Response("Not Found", { status: 404 });
}
//in case of using   const _error = useRouteError();
//_message = JSON.parse(_error.data).message
//@ts-ignore
import { showAlert } from "../../utility/imports.js";
