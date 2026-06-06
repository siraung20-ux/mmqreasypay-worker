export default {
  async fetch(request) {

    return new Response(
      JSON.stringify({
        method: request.method,
        url: request.url
      }),
      {
        headers: {
          "content-type": "application/json"
        }
      }
    );
  }
}
