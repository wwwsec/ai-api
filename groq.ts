import { serve } from "https://deno.land/std/http/server.ts";

const TARGET_URL = "https://api.groq.com";// 将此替换为您要转发的目标域名

const handler = async (request: Request) => {
    const url = new URL(request.url);
    const targetUrl = new URL(TARGET_URL + url.pathname + url.search);

    const response = await fetch(targetUrl.toString(), {
        method: request.method,
        headers: request.headers,
        body: request.body,
    });

    return new Response(response.body, {
        status: response.status,
        headers: response.headers,
    });
};

console.log("Server running on http://localhost:80");
await serve(handler);