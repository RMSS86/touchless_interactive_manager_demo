type CustomRequestInit = Omit<RequestInit, "body"> & {
  /**
   * @description
   * REQUEST CLIENT WILL RECIEIVE BOY IN JSON AND  JSON.stringify BEFORE SENT TO SERVER
   */
  body?: any;
};

//> FUNCTION DECLARATION
export const request = async <T>(
  //< iINPUTS
  endpoint: string,
  customConfig: CustomRequestInit = {}
): Promise<T> => {
  //> OPTIONS
  const headers = {
    "content-type": "application/json",
  };

  const method = customConfig.method || (customConfig.body ? "POST" : "GET");

  const config: RequestInit = {
    // If the user provided a request body, default to POST, but this can be ovewritten by user when they call: client('..', {method: 'PUT', body: ''})
    method,
    ...customConfig,
    headers: {
      ...headers,
      ...customConfig.headers,
    },
  };

  if (customConfig.body) {
    config.body = JSON.stringify(customConfig.body);
  }

  //< DIALER ON RESPONSE
  const response = await window.fetch(endpoint, config).catch((error) => {
    return Promise.reject(new Error(error));
  });

  /*
      "By default, window.fetch will only reject a promise if the actual request itself failed (network error),
      not if it returned a "Client error response". Luckily, the Response object has an ok property which
      we can use to reject the promise in our wrapper"
      - https://kentcdodds.com/blog/replace-axios-with-a-simple-custom-fetch-wrapper
    */

  //> RESPONSE OK HANDLING
  if (response.ok) {
    const data = await response.json();

    return data as T;
  } else {
    //> ERROR HANDLING
    const errorMessage = await response.text();
    return Promise.reject(new Error(errorMessage));
  }

  /**
   * @description
   * `fetch` based API client, with more robust error handling. Please read the article below for the details.
   *
   * Implementation inspiration: https://kentcdodds.com/blog/replace-axios-with-a-simple-custom-fetch-wrapper
   * Typescript explanation: https://stackoverflow.com/a/49471725/2971795
   * @example
   * const example1 = await client<put_type_shape_here>('/some_enpoint');
   * const example2 = await client<People[]>('/people');
   */
};

//////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////

// type CustomRequestInit = Omit<RequestInit, "body"> & {
//     /**
//      * @description
//      * For our `request` client, allow the user to pass in JSON data to the body & we will automatically
//      * JSON.stringify it before sending it ot the server.
//      */
//     body?: any;
//   };

//   export const request = async <T>(
//     endpoint: string,
//     customConfig: CustomRequestInit = {}
//   ): Promise<T> => {
//     const headers = {
//       "content-type": "application/json",
//     };

//     const method = customConfig.method || (customConfig.body ? "POST" : "GET");

//     const config: RequestInit = {
//       // If the user provided a request body, default to POST, but this can be ovewritten by user when they call: client('..', {method: 'PUT', body: ''})
//       method,
//       ...customConfig,
//       headers: {
//         ...headers,
//         ...customConfig.headers,
//       },
//     };

//     if (customConfig.body) {
//       config.body = JSON.stringify(customConfig.body);
//     }

//     const response = await window.fetch(endpoint, config).catch((error) => {
//       return Promise.reject(new Error(error));
//     });

//     /*
//         "By default, window.fetch will only reject a promise if the actual request itself failed (network error),
//         not if it returned a "Client error response". Luckily, the Response object has an ok property which
//         we can use to reject the promise in our wrapper"
//         - https://kentcdodds.com/blog/replace-axios-with-a-simple-custom-fetch-wrapper
//       */
//     if (response.ok) {
//       const data = await response.json();

//       return data as T;
//     } else {
//       const errorMessage = await response.text();

//       return Promise.reject(new Error(errorMessage));
//     }

//     /**
//      * @description
//      * `fetch` based API client, with more robust error handling. Please read the article below for the details.
//      *
//      * Implementation inspiration: https://kentcdodds.com/blog/replace-axios-with-a-simple-custom-fetch-wrapper
//      * Typescript explanation: https://stackoverflow.com/a/49471725/2971795
//      * @example
//      * const example1 = await client<put_type_shape_here>('/some_enpoint');
//      * const example2 = await client<People[]>('/people');
//      */
//   };
