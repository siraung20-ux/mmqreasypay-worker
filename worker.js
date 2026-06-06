export default {
  async fetch(request, env) {

    if (request.method !== "POST") {
      return new Response("VERSION TEST 123");
    }

    try {
      const body = await request.text();

      return new Response(body, {
        headers: {
          "content-type": "application/json"
        }
      });

    } catch (e) {
      return new Response(e.toString());
    }
  }
}
