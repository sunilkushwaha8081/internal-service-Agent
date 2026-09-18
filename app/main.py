# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# from pydantic import BaseModel

# from app.agent import run_agent


# app = FastAPI(
#     title="IT Service Desk Agent",
#     description="Employee IT Support Agent",
#     version="1.0.0"
# )


# class EmployeeRequest(BaseModel):
#     message: str


# HTML_PAGE = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">

#     <title>IT Service Desk Agent</title>

#     <style>
#         * {
#             box-sizing: border-box;
#         }

#         body {
#             margin: 0;
#             min-height: 100vh;
#             background: #0d1118;
#             color: #f1f5f9;
#             font-family:
#                 Inter,
#                 -apple-system,
#                 BlinkMacSystemFont,
#                 "Segoe UI",
#                 sans-serif;
#         }

#         .app {
#             max-width: 1100px;
#             margin: 0 auto;
#             padding: 28px 24px 50px;
#         }

#         /* Header */

#         .header {
#             margin-bottom: 26px;
#         }

#         .brand {
#             display: flex;
#             align-items: center;
#             gap: 10px;
#             font-size: 28px;
#             font-weight: 700;
#             letter-spacing: -0.5px;
#         }

#         .brand-icon {
#             width: 36px;
#             height: 36px;
#             border-radius: 10px;
#             background: #4f86f7;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             font-size: 19px;
#         }

#         .subtitle {
#             color: #71809a;
#             margin-top: 7px;
#             font-size: 14px;
#         }

#         /* Employee */

#         .employee-section {
#             border-bottom: 1px solid #293342;
#             padding-bottom: 22px;
#             margin-bottom: 24px;
#         }

#         .employee-label {
#             color: #9aa8bd;
#             font-size: 14px;
#             margin-right: 10px;
#         }

#         .employee-input {
#             width: 150px;
#             background: #19212d;
#             border: 1px solid #303b4d;
#             color: #f1f5f9;
#             border-radius: 8px;
#             padding: 10px 12px;
#             outline: none;
#         }

#         .employee-input:focus {
#             border-color: #4f86f7;
#         }

#         /* Conversation */

#         .conversation-card {
#             background: #171f2b;
#             border: 1px solid #2c3748;
#             border-radius: 15px;
#             overflow: hidden;
#             box-shadow: 0 10px 30px rgba(0,0,0,0.12);
#         }

#         .conversation-header {
#             height: 58px;
#             padding: 0 20px;
#             display: flex;
#             align-items: center;
#             justify-content: space-between;
#             border-bottom: 1px solid #2c3748;
#         }

#         .conversation-title {
#             font-size: 16px;
#             font-weight: 700;
#         }

#         .new-request {
#             border: 0;
#             background: transparent;
#             color: #667994;
#             cursor: pointer;
#             font-size: 13px;
#         }

#         .new-request:hover {
#             color: #9db7e8;
#         }

#         /* Messages */

#         .messages {
#             height: 390px;
#             overflow-y: auto;
#             padding: 18px;
#         }

#         .message-row {
#             display: flex;
#             margin-bottom: 18px;
#         }

#         .message-row.user {
#             justify-content: flex-end;
#         }

#         .message {
#             max-width: 78%;
#             padding: 13px 15px;
#             border-radius: 12px;
#             line-height: 1.5;
#             font-size: 14px;
#             white-space: pre-wrap;
#         }

#         .agent-message {
#             background: #202a38;
#             border: 1px solid #2d394b;
#         }

#         .user-message {
#             background: #3978ed;
#             color: white;
#         }

#         .message-meta {
#             font-size: 11px;
#             color: #62738d;
#             margin-top: 6px;
#         }

#         .user .message-meta {
#             text-align: right;
#         }

#         .status-box {
#             margin-top: 10px;
#             padding: 10px 12px;
#             border-radius: 8px;
#             background: #111720;
#             border: 1px solid #303c4d;
#             font-size: 12px;
#             color: #aebbd0;
#         }

#         /* Input */

#         .input-area {
#             display: flex;
#             gap: 10px;
#             padding: 15px 18px;
#             border-top: 1px solid #2c3748;
#         }

#         .message-input {
#             flex: 1;
#             min-width: 0;
#             height: 44px;
#             padding: 0 14px;
#             border-radius: 9px;
#             border: 1px solid #303b4d;
#             background: #0f141c;
#             color: #f1f5f9;
#             outline: none;
#             font-size: 14px;
#         }

#         .message-input::placeholder {
#             color: #627087;
#         }

#         .message-input:focus {
#             border-color: #4f86f7;
#         }

#         .send-button {
#             height: 44px;
#             padding: 0 22px;
#             border: none;
#             border-radius: 9px;
#             background: #4b82ef;
#             color: white;
#             font-size: 14px;
#             font-weight: 600;
#             cursor: pointer;
#         }

#         .send-button:hover {
#             background: #5b8ff2;
#         }

#         .send-button:disabled {
#             opacity: 0.5;
#             cursor: not-allowed;
#         }

#         /* Loading */

#         .typing {
#             color: #73839b;
#             font-size: 13px;
#             padding: 5px 2px;
#         }

#         /* Responsive */

#         @media (max-width: 650px) {
#             .app {
#                 padding: 20px 14px;
#             }

#             .messages {
#                 height: 420px;
#             }

#             .message {
#                 max-width: 90%;
#             }

#             .send-button {
#                 padding: 0 15px;
#             }
#         }
#     </style>
# </head>

# <body>

# <div class="app">

#     <div class="header">
#         <div class="brand">
#             <div class="brand-icon">IT</div>
#             <div>IT Service Desk</div>
#         </div>

#         <div class="subtitle">
#             Describe an issue below — the desk agent will triage, resolve, or route it.
#         </div>
#     </div>


#     <div class="employee-section">
#         <span class="employee-label">Your name</span>

#         <input
#             id="employeeName"
#             class="employee-input"
#             value="Employee"
#             placeholder="Your name"
#         >
#     </div>


#     <div class="conversation-card">

#         <div class="conversation-header">
#             <div class="conversation-title">
#                 Conversation
#             </div>

#             <button
#                 class="new-request"
#                 onclick="newRequest()"
#             >
#                 New request
#             </button>
#         </div>


#         <div
#             id="messages"
#             class="messages"
#         >

#             <div class="message-row">
#                 <div>
#                     <div class="message agent-message">
#                         Hi — I'm the IT desk agent. Tell me what's going on and I'll sort out the fastest path to a fix.
#                     </div>

#                     <div class="message-meta">
#                         Desk agent · <span id="time"></span>
#                     </div>
#                 </div>
#             </div>

#         </div>


#         <div class="input-area">

#             <input
#                 id="messageInput"
#                 class="message-input"
#                 placeholder="Describe your issue..."
#                 autocomplete="off"
#             >

#             <button
#                 id="sendButton"
#                 class="send-button"
#                 onclick="sendMessage()"
#             >
#                 Send
#             </button>

#         </div>

#     </div>

# </div>


# <script>

# function currentTime() {
#     return new Date().toLocaleTimeString([], {
#         hour: "2-digit",
#         minute: "2-digit"
#     });
# }


# document.getElementById("time").textContent = currentTime();


# const input = document.getElementById("messageInput");

# input.addEventListener("keydown", function(event) {

#     if (event.key === "Enter") {
#         event.preventDefault();
#         sendMessage();
#     }

# });


# function addMessage(text, type, statusData = null) {

#     const messages = document.getElementById("messages");

#     const row = document.createElement("div");

#     row.className = "message-row " +
#         (type === "user" ? "user" : "");


#     const wrapper = document.createElement("div");


#     const message = document.createElement("div");

#     message.className =
#         "message " +
#         (type === "user"
#             ? "user-message"
#             : "agent-message");


#     message.textContent = text;


#     wrapper.appendChild(message);


#     const meta = document.createElement("div");

#     meta.className = "message-meta";

#     meta.textContent =
#         type === "user"
#             ? `${document.getElementById("employeeName").value || "Employee"} · ${currentTime()}`
#             : `Desk agent · ${currentTime()}`;


#     wrapper.appendChild(meta);


#     if (statusData) {

#         const status = document.createElement("div");

#         status.className = "status-box";

#         let details =
#             "Status: " +
#             (statusData.status || "UNKNOWN");


#         if (statusData.category) {
#             details +=
#                 " · Category: " +
#                 statusData.category;
#         }


#         if (statusData.source) {
#             details +=
#                 "\\nSource: " +
#                 statusData.source;
#         }


#         if (statusData.ticket_id) {
#             details +=
#                 "\\nTicket ID: " +
#                 statusData.ticket_id;
#         }


#         status.textContent = details;

#         wrapper.appendChild(status);
#     }


#     row.appendChild(wrapper);

#     messages.appendChild(row);

#     messages.scrollTop = messages.scrollHeight;
# }


# async function sendMessage() {

#     const input =
#         document.getElementById("messageInput");

#     const button =
#         document.getElementById("sendButton");


#     const message =
#         input.value.trim();


#     if (!message) {
#         return;
#     }


#     addMessage(
#         message,
#         "user"
#     );


#     input.value = "";

#     button.disabled = true;

#     button.textContent = "Sending...";


#     const messages =
#         document.getElementById("messages");


#     const typing =
#         document.createElement("div");

#     typing.className = "typing";

#     typing.id = "typing";

#     typing.textContent =
#         "Desk agent is thinking...";


#     messages.appendChild(typing);

#     messages.scrollTop = messages.scrollHeight;


#     try {

#         const response =
#             await fetch("/support", {

#                 method: "POST",

#                 headers: {
#                     "Content-Type":
#                         "application/json"
#                 },

#                 body: JSON.stringify({
#                     message: message
#                 })

#             });


#         const data =
#             await response.json();


#         const typingElement =
#             document.getElementById("typing");


#         if (typingElement) {
#             typingElement.remove();
#         }


#         addMessage(
#            data.resolution || data.message || "No response received.",
#             "agent",
#             data
#         );


#     } catch (error) {

#         const typingElement =
#             document.getElementById("typing");


#         if (typingElement) {
#             typingElement.remove();
#         }


#         addMessage(
#             "I couldn't connect to the IT service. Please try again.",
#             "agent"
#         );

#     }


#     button.disabled = false;

#     button.textContent = "Send";

#     input.focus();
# }


# function newRequest() {

#     const messages =
#         document.getElementById("messages");


#     messages.innerHTML = `
#         <div class="message-row">
#             <div>
#                 <div class="message agent-message">
#                     Hi — I'm the IT desk agent. Tell me what's going on and I'll sort out the fastest path to a fix.
#                 </div>

#                 <div class="message-meta">
#                     Desk agent · ${currentTime()}
#                 </div>
#             </div>
#         </div>
#     `;

#     document.getElementById("messageInput").value = "";

#     document.getElementById("messageInput").focus();
# }

# </script>

# </body>
# </html>
# """


# @app.get("/", response_class=HTMLResponse)
# def home():
#     return HTML_PAGE


# @app.post("/support")
# def support(request: EmployeeRequest):
#     return run_agent(request.message)





# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# from pydantic import BaseModel

# from app.agent import run_agent


# app = FastAPI(title="IT Service Desk")


# class EmployeeRequest(BaseModel):
#     message: str


# HTML_PAGE = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">

#     <title>IT Service Desk</title>

#     <style>
#         * {
#             box-sizing: border-box;
#         }

#         body {
#             margin: 0;
#             font-family:
#                 Inter,
#                 ui-sans-serif,
#                 system-ui,
#                 -apple-system,
#                 BlinkMacSystemFont,
#                 "Segoe UI",
#                 sans-serif;

#             background: #f4f6f8;
#             color: #172033;
#         }

#         .app {
#             min-height: 100vh;
#             display: flex;
#         }

#         /* =========================
#            SIDEBAR
#         ========================= */

#         .sidebar {
#             width: 250px;
#             background: #111827;
#             color: white;
#             padding: 24px 18px;
#             display: flex;
#             flex-direction: column;
#         }

#         .brand {
#             display: flex;
#             align-items: center;
#             gap: 12px;
#             padding: 6px 8px 28px;
#         }

#         .brand-icon {
#             width: 40px;
#             height: 40px;
#             border-radius: 11px;
#             background: #2563eb;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             font-size: 19px;
#             font-weight: 700;
#         }

#         .brand-text h2 {
#             margin: 0;
#             font-size: 17px;
#         }

#         .brand-text p {
#             margin: 3px 0 0;
#             font-size: 11px;
#             color: #9ca3af;
#         }

#         .new-request {
#             width: 100%;
#             border: 0;
#             border-radius: 10px;
#             padding: 12px;
#             background: #2563eb;
#             color: white;
#             font-size: 14px;
#             font-weight: 600;
#             cursor: pointer;
#             transition: 0.2s;
#         }

#         .new-request:hover {
#             background: #1d4ed8;
#         }

#         .sidebar-section {
#             margin-top: 30px;
#         }

#         .sidebar-title {
#             padding: 0 8px;
#             margin-bottom: 10px;
#             color: #6b7280;
#             font-size: 11px;
#             text-transform: uppercase;
#             letter-spacing: 0.08em;
#         }

#         .sidebar-item {
#             padding: 10px 9px;
#             border-radius: 8px;
#             color: #d1d5db;
#             font-size: 13px;
#             margin-bottom: 3px;
#         }

#         .sidebar-item.active {
#             background: #1f2937;
#             color: white;
#         }

#         .sidebar-footer {
#             margin-top: auto;
#             padding: 14px 8px;
#             border-top: 1px solid #263142;
#             color: #9ca3af;
#             font-size: 11px;
#         }

#         /* =========================
#            MAIN
#         ========================= */

#         .main {
#             flex: 1;
#             display: flex;
#             flex-direction: column;
#             min-width: 0;
#         }

#         .topbar {
#             height: 72px;
#             background: white;
#             border-bottom: 1px solid #e5e7eb;
#             display: flex;
#             align-items: center;
#             justify-content: space-between;
#             padding: 0 34px;
#         }

#         .topbar-title h1 {
#             margin: 0;
#             font-size: 20px;
#             font-weight: 700;
#         }

#         .topbar-title p {
#             margin: 4px 0 0;
#             font-size: 12px;
#             color: #6b7280;
#         }

#         .status-online {
#             display: flex;
#             align-items: center;
#             gap: 7px;
#             padding: 7px 11px;
#             background: #f0fdf4;
#             border: 1px solid #bbf7d0;
#             color: #15803d;
#             border-radius: 20px;
#             font-size: 12px;
#             font-weight: 600;
#         }

#         .online-dot {
#             width: 7px;
#             height: 7px;
#             border-radius: 50%;
#             background: #22c55e;
#         }

#         /* =========================
#            CONTENT
#         ========================= */

#         .content {
#             width: min(1050px, 94%);
#             margin: 28px auto;
#             flex: 1;
#             display: flex;
#             flex-direction: column;
#         }

#         .welcome-card {
#             background: white;
#             border: 1px solid #e5e7eb;
#             border-radius: 14px;
#             padding: 20px 22px;
#             margin-bottom: 18px;
#             box-shadow: 0 2px 7px rgba(15, 23, 42, 0.04);
#         }

#         .welcome-card h2 {
#             margin: 0 0 6px;
#             font-size: 16px;
#         }

#         .welcome-card p {
#             margin: 0;
#             font-size: 13px;
#             color: #6b7280;
#             line-height: 1.6;
#         }

#         .employee-row {
#             display: flex;
#             align-items: center;
#             gap: 12px;
#             margin-top: 16px;
#         }

#         .employee-label {
#             font-size: 12px;
#             color: #6b7280;
#             white-space: nowrap;
#         }

#         .employee-input {
#             flex: 1;
#             max-width: 280px;
#             border: 1px solid #d1d5db;
#             border-radius: 8px;
#             padding: 9px 11px;
#             outline: none;
#             font-size: 13px;
#         }

#         .employee-input:focus {
#             border-color: #2563eb;
#             box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.08);
#         }

#         /* =========================
#            CHAT
#         ========================= */

#         .chat-card {
#             flex: 1;
#             min-height: 470px;
#             background: white;
#             border: 1px solid #e5e7eb;
#             border-radius: 14px;
#             box-shadow: 0 2px 7px rgba(15, 23, 42, 0.04);
#             display: flex;
#             flex-direction: column;
#             overflow: hidden;
#         }

#         .chat-header {
#             padding: 15px 20px;
#             border-bottom: 1px solid #edf0f3;
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#         }

#         .agent-info {
#             display: flex;
#             align-items: center;
#             gap: 10px;
#         }

#         .agent-avatar {
#             width: 34px;
#             height: 34px;
#             border-radius: 9px;
#             background: #eff6ff;
#             color: #2563eb;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             font-weight: 700;
#             font-size: 13px;
#         }

#         .agent-name {
#             font-size: 13px;
#             font-weight: 700;
#         }

#         .agent-role {
#             margin-top: 2px;
#             font-size: 11px;
#             color: #9ca3af;
#         }

#         .chat-label {
#             font-size: 11px;
#             color: #9ca3af;
#         }

#         .messages {
#             flex: 1;
#             overflow-y: auto;
#             padding: 24px;
#             background: #fafbfc;
#         }

#         .message-row {
#             display: flex;
#             margin-bottom: 20px;
#         }

#         .message-row.user {
#             justify-content: flex-end;
#         }

#         .message {
#             max-width: 72%;
#             padding: 12px 15px;
#             border-radius: 12px;
#             font-size: 13px;
#             line-height: 1.65;
#             white-space: pre-wrap;
#         }

#         .message.agent {
#             background: white;
#             border: 1px solid #e5e7eb;
#             color: #374151;
#             border-top-left-radius: 4px;
#         }

#         .message.user {
#             background: #2563eb;
#             color: white;
#             border-top-right-radius: 4px;
#         }

#         .message-time {
#             margin-top: 5px;
#             font-size: 10px;
#             color: #9ca3af;
#         }

#         .user .message-time {
#             text-align: right;
#         }

#         /* =========================
#            TICKET CARD
#         ========================= */

#         .ticket-card {
#             margin-top: 10px;
#             border: 1px solid #e5e7eb;
#             background: white;
#             border-radius: 10px;
#             padding: 13px;
#             font-size: 12px;
#         }

#         .ticket-title {
#             font-weight: 700;
#             margin-bottom: 10px;
#         }

#         .ticket-grid {
#             display: grid;
#             grid-template-columns: 1fr 1fr;
#             gap: 8px;
#         }

#         .ticket-item {
#             padding: 8px;
#             background: #f8fafc;
#             border-radius: 7px;
#         }

#         .ticket-item span {
#             display: block;
#             color: #9ca3af;
#             font-size: 10px;
#             margin-bottom: 3px;
#         }

#         .ticket-item strong {
#             font-size: 11px;
#         }

#         .badge {
#             display: inline-block;
#             padding: 3px 7px;
#             border-radius: 5px;
#             font-size: 10px;
#             font-weight: 700;
#         }

#         .badge-red {
#             background: #fef2f2;
#             color: #dc2626;
#         }

#         .badge-green {
#             background: #f0fdf4;
#             color: #15803d;
#         }

#         /* =========================
#            INPUT
#         ========================= */

#         .input-area {
#             padding: 16px;
#             border-top: 1px solid #e5e7eb;
#             background: white;
#         }

#         .input-box {
#             display: flex;
#             align-items: flex-end;
#             gap: 10px;
#         }

#         textarea {
#             flex: 1;
#             resize: none;
#             min-height: 45px;
#             max-height: 120px;
#             border: 1px solid #d1d5db;
#             border-radius: 9px;
#             padding: 12px;
#             font-family: inherit;
#             font-size: 13px;
#             outline: none;
#         }

#         textarea:focus {
#             border-color: #2563eb;
#             box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.08);
#         }

#         .send-button {
#             height: 45px;
#             padding: 0 20px;
#             border: 0;
#             border-radius: 9px;
#             background: #2563eb;
#             color: white;
#             font-size: 13px;
#             font-weight: 600;
#             cursor: pointer;
#         }

#         .send-button:hover {
#             background: #1d4ed8;
#         }

#         .send-button:disabled {
#             opacity: 0.6;
#             cursor: not-allowed;
#         }

#         .hint {
#             margin-top: 8px;
#             font-size: 10px;
#             color: #9ca3af;
#             text-align: center;
#         }

#         .typing {
#             display: none;
#             align-items: center;
#             gap: 6px;
#             color: #9ca3af;
#             font-size: 11px;
#             margin-bottom: 14px;
#         }

#         .typing.show {
#             display: flex;
#         }

#         .typing-dot {
#             width: 5px;
#             height: 5px;
#             border-radius: 50%;
#             background: #9ca3af;
#             animation: blink 1.2s infinite;
#         }

#         .typing-dot:nth-child(2) {
#             animation-delay: 0.15s;
#         }

#         .typing-dot:nth-child(3) {
#             animation-delay: 0.3s;
#         }

#         @keyframes blink {
#             0%, 80%, 100% {
#                 opacity: 0.25;
#             }
#             40% {
#                 opacity: 1;
#             }
#         }

#         /* =========================
#            MOBILE
#         ========================= */

#         @media (max-width: 760px) {
#             .sidebar {
#                 display: none;
#             }

#             .topbar {
#                 padding: 0 18px;
#             }

#             .content {
#                 width: 94%;
#                 margin: 18px auto;
#             }

#             .message {
#                 max-width: 88%;
#             }

#             .employee-row {
#                 align-items: flex-start;
#                 flex-direction: column;
#             }

#             .employee-input {
#                 max-width: none;
#                 width: 100%;
#             }
#         }
#     </style>
# </head>

# <body>

# <div class="app">

#     <!-- SIDEBAR -->

#     <aside class="sidebar">

#         <div class="brand">

#             <div class="brand-icon">
#                 IT
#             </div>

#             <div class="brand-text">
#                 <h2>Service Desk</h2>
#                 <p>Internal Support</p>
#             </div>

#         </div>

#         <button
#             class="new-request"
#             onclick="newRequest()"
#         >
#             + New Request
#         </button>

#         <div class="sidebar-section">

#             <div class="sidebar-title">
#                 Workspace
#             </div>

#             <div class="sidebar-item active">
#                 💬 Current Request
#             </div>

#             <div class="sidebar-item">
#                 🎫 My Tickets
#             </div>

#             <div class="sidebar-item">
#                 📚 Knowledge Base
#             </div>

#         </div>

#         <div class="sidebar-section">

#             <div class="sidebar-title">
#                 Support
#             </div>

#             <div class="sidebar-item">
#                 🔐 Security
#             </div>

#             <div class="sidebar-item">
#                 💻 Hardware
#             </div>

#             <div class="sidebar-item">
#                 🌐 Network
#             </div>

#         </div>

#         <div class="sidebar-footer">
#             Internal IT Service Desk<br>
#             Agent status: Online
#         </div>

#     </aside>


#     <!-- MAIN -->

#     <main class="main">

#         <header class="topbar">

#             <div class="topbar-title">

#                 <h1>IT Service Desk</h1>

#                 <p>
#                     Describe an issue below — the desk agent will triage,
#                     resolve, or route it.
#                 </p>

#             </div>

#             <div class="status-online">
#                 <span class="online-dot"></span>
#                 Agent Online
#             </div>

#         </header>


#         <section class="content">

#             <!-- WELCOME -->

#             <div class="welcome-card">

#                 <h2>
#                     How can we help?
#                 </h2>

#                 <p>
#                     Tell us what you're experiencing. The service desk agent
#                     will check approved internal policies and provide guidance
#                     or create a support ticket when escalation is required.
#                 </p>

#                 <div class="employee-row">

#                     <div class="employee-label">
#                         Your name
#                     </div>

#                     <input
#                         id="employeeName"
#                         class="employee-input"
#                         type="text"
#                         placeholder="Enter your name"
#                     >

#                 </div>

#             </div>


#             <!-- CHAT -->

#             <div class="chat-card">

#                 <div class="chat-header">

#                     <div class="agent-info">

#                         <div class="agent-avatar">
#                             AI
#                         </div>

#                         <div>
#                             <div class="agent-name">
#                                 IT Support Agent
#                             </div>

#                             <div class="agent-role">
#                                 Automated Internal Support
#                             </div>
#                         </div>

#                     </div>

#                     <div class="chat-label">
#                         Secure support channel
#                     </div>

#                 </div>


#                 <div
#                     id="messages"
#                     class="messages"
#                 >

#                     <div class="message-row">

#                         <div>

#                             <div class="message agent">
#                                 Hello! I'm your IT Service Desk agent.
#                                 Please describe the issue you're experiencing
#                                 and I'll check the appropriate internal
#                                 procedure.
#                             </div>

#                             <div class="message-time">
#                                 IT Support Agent · Now
#                             </div>

#                         </div>

#                     </div>

#                 </div>


#                 <div class="input-area">

#                     <div
#                         id="typing"
#                         class="typing"
#                     >
#                         <span>Agent is checking the request</span>
#                         <span class="typing-dot"></span>
#                         <span class="typing-dot"></span>
#                         <span class="typing-dot"></span>
#                     </div>

#                     <div class="input-box">

#                         <textarea
#                             id="messageInput"
#                             placeholder="Describe your IT issue..."
#                             rows="1"
#                         ></textarea>

#                         <button
#                             id="sendButton"
#                             class="send-button"
#                             onclick="sendMessage()"
#                         >
#                             Send
#                         </button>

#                     </div>

#                     <div class="hint">
#                         Do not share passwords, MFA codes, or other sensitive credentials.
#                     </div>

#                 </div>

#             </div>

#         </section>

#     </main>

# </div>


# <script>

#     const input = document.getElementById("messageInput");
#     const sendButton = document.getElementById("sendButton");
#     const messages = document.getElementById("messages");
#     const typing = document.getElementById("typing");


#     function currentTime() {

#         return new Date().toLocaleTimeString(
#             [],
#             {
#                 hour: "2-digit",
#                 minute: "2-digit"
#             }
#         );

#     }


#     function addMessage(
#         text,
#         type,
#         data = null
#     ) {

#         const row = document.createElement("div");

#         row.className =
#             "message-row " +
#             (type === "user" ? "user" : "");


#         const wrapper = document.createElement("div");


#         const bubble = document.createElement("div");

#         bubble.className =
#             "message " +
#             (type === "user" ? "user" : "agent");

#         bubble.textContent = text;


#         const time = document.createElement("div");

#         time.className = "message-time";

#         time.textContent =
#             (type === "user"
#                 ? "You"
#                 : "IT Support Agent")
#             + " · "
#             + currentTime();


#         wrapper.appendChild(bubble);
#         wrapper.appendChild(time);


#         // Ticket details for escalated requests

#         if (
#             type === "agent" &&
#             data &&
#             data.status === "ESCALATED"
#         ) {

#             const ticket =
#                 data.ticket || {};


#             const ticketCard =
#                 document.createElement("div");

#             ticketCard.className =
#                 "ticket-card";


#             const title =
#                 document.createElement("div");

#             title.className =
#                 "ticket-title";

#             title.textContent =
#                 "🎫 Support Ticket Created";


#             const grid =
#                 document.createElement("div");

#             grid.className =
#                 "ticket-grid";


#             grid.innerHTML = `

#                 <div class="ticket-item">
#                     <span>Ticket ID</span>
#                     <strong>
#                         ${escapeHtml(
#                             data.ticket_id ||
#                             ticket.ticket_id ||
#                             "Created"
#                         )}
#                     </strong>
#                 </div>

#                 <div class="ticket-item">
#                     <span>Status</span>
#                     <strong>
#                         <span class="badge badge-red">
#                             ESCALATED
#                         </span>
#                     </strong>
#                 </div>

#                 <div class="ticket-item">
#                     <span>Category</span>
#                     <strong>
#                         ${escapeHtml(
#                             data.category ||
#                             ticket.category ||
#                             "IT Support"
#                         )}
#                     </strong>
#                 </div>

#                 <div class="ticket-item">
#                     <span>Priority</span>
#                     <strong>
#                         ${escapeHtml(
#                             ticket.priority ||
#                             "MEDIUM"
#                         )}
#                     </strong>
#                 </div>

#             `;


#             ticketCard.appendChild(title);
#             ticketCard.appendChild(grid);

#             wrapper.appendChild(ticketCard);

#         }


#         row.appendChild(wrapper);

#         messages.appendChild(row);

#         messages.scrollTop =
#             messages.scrollHeight;

#     }


#     function escapeHtml(value) {

#         return String(value)
#             .replaceAll("&", "&amp;")
#             .replaceAll("<", "&lt;")
#             .replaceAll(">", "&gt;")
#             .replaceAll('"', "&quot;")
#             .replaceAll("'", "&#039;");

#     }


#     async function sendMessage() {

#         const message =
#             input.value.trim();


#         if (!message) {

#             return;

#         }


#         addMessage(
#             message,
#             "user"
#         );


#         input.value = "";

#         input.style.height = "45px";

#         sendButton.disabled = true;

#         typing.classList.add("show");


#         try {

#             const response =
#                 await fetch(
#                     "/support",
#                     {
#                         method: "POST",

#                         headers: {
#                             "Content-Type":
#                                 "application/json"
#                         },

#                         body: JSON.stringify({
#                             message: message
#                         })
#                     }
#                 );


#             const data =
#                 await response.json();


#             typing.classList.remove("show");


#             if (!response.ok) {

#                 throw new Error(
#                     data.detail ||
#                     "Request failed"
#                 );

#             }


#             addMessage(

#                 data.resolution ||
#                 data.message ||
#                 "No response received.",

#                 "agent",

#                 data

#             );


#         } catch (error) {

#             typing.classList.remove("show");

#             addMessage(
#                 "Sorry, I couldn't process the request right now.",
#                 "agent"
#             );

#             console.error(error);

#         }


#         sendButton.disabled = false;

#         input.focus();

#     }


#     function newRequest() {

#         messages.innerHTML = `

#             <div class="message-row">

#                 <div>

#                     <div class="message agent">
#                         Hello! I'm your IT Service Desk agent.
#                         Please describe the issue you're experiencing
#                         and I'll check the appropriate internal procedure.
#                     </div>

#                     <div class="message-time">
#                         IT Support Agent · Now
#                     </div>

#                 </div>

#             </div>

#         `;

#         input.value = "";

#         input.focus();

#     }


#     input.addEventListener(
#         "keydown",
#         function(event) {

#             if (
#                 event.key === "Enter" &&
#                 !event.shiftKey
#             ) {

#                 event.preventDefault();

#                 sendMessage();

#             }

#         }
#     );


#     input.addEventListener(
#         "input",
#         function() {

#             this.style.height = "45px";

#             this.style.height =
#                 Math.min(
#                     this.scrollHeight,
#                     120
#                 ) + "px";

#         }
#     );

# </script>

# </body>
# </html>
# """


# @app.get("/", response_class=HTMLResponse)
# def home():
#     return HTML_PAGE


# @app.post("/support")
# def support(request: EmployeeRequest):
#     return run_agent(request.message)





from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from app.agent import run_agent


app = FastAPI(title="Veridian Corp - IT Service Desk")


class EmployeeRequest(BaseModel):
    message: str


# ============================================================
# ASSIGNMENT 2 — EXISTING TICKET QUEUE
# ============================================================

TICKET_QUEUE = [
    {
        "id": "TK-1042",
        "employee": "R. Verma",
        "issue": "VPN credential expired",
        "status": "Resolved (closed)",
    },
    {
        "id": "TK-1043",
        "employee": "S. Iyer",
        "issue": "Laptop replacement (3.2 yrs old)",
        "status": "Approved — pending fulfillment (active)",
    },
    {
        "id": "TK-1044",
        "employee": "A. Khan",
        "issue": "Non-catalog software request",
        "status": "Pending Security review (active)",
    },
    {
        "id": "TK-1045",
        "employee": "P. Joshi",
        "issue": "Mailbox quota increase",
        "status": "Approved at 35GB (closed)",
    },
    {
        "id": "TK-1046",
        "employee": "M. Das",
        "issue": "Printer paper jam, floor 2",
        "status": "Resolved (closed)",
    },
    {
        "id": "TK-1047",
        "employee": "K. Singh",
        "issue": "Home office equipment request",
        "status": "Pending Finance (active)",
    },
    {
        "id": "TK-1048",
        "employee": "T. Rao",
        "issue": "Phishing email reported",
        "status": "Escalated to Security — under investigation (active)",
    },
    {
        "id": "TK-1049",
        "employee": "V. Nambiar",
        "issue": "Password reset",
        "status": "Resolved (closed)",
    },
    {
        "id": "TK-1050",
        "employee": "J. Fernandes",
        "issue": "Admin access request",
        "status": "Rejected — no business justification provided (closed)",
    },
    {
        "id": "TK-1051",
        "employee": "L. Menon",
        "issue": "Guest Wi-Fi issued",
        "status": "Resolved (closed)",
    },
]


# ============================================================
# PROFESSIONAL UI
# ============================================================

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<title>Veridian Corp — IT Service Desk</title>


<style>

/* ============================================================
   RESET
============================================================ */

* {
    box-sizing: border-box;
}

body {
    margin: 0;

    font-family:
        Inter,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        Roboto,
        Arial,
        sans-serif;

    background: #f4f6f8;

    color: #1f2937;
}


/* ============================================================
   HEADER
============================================================ */

.header {
    height: 70px;

    background: #ffffff;

    border-bottom: 1px solid #dfe3e8;

    display: flex;

    align-items: center;

    justify-content: space-between;

    padding: 0 42px;
}


.logo-area {
    display: flex;

    align-items: center;

    gap: 13px;
}


.logo {
    width: 38px;
    height: 38px;

    border-radius: 7px;

    background: #17365d;

    color: #ffffff;

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 13px;

    font-weight: 700;

    letter-spacing: .4px;
}


.company {
    font-size: 15px;

    font-weight: 700;

    color: #172033;
}


.company-subtitle {
    margin-top: 2px;

    font-size: 11px;

    color: #7b8491;
}


.header-right {
    display: flex;

    align-items: center;

    gap: 16px;
}


.period {
    font-size: 11px;

    color: #7b8491;
}


.online {
    display: flex;

    align-items: center;

    gap: 7px;

    padding: 6px 10px;

    border-radius: 15px;

    background: #eef8f1;

    color: #257a43;

    font-size: 11px;

    font-weight: 600;
}


.online-dot {
    width: 7px;
    height: 7px;

    border-radius: 50%;

    background: #35a854;
}


/* ============================================================
   PAGE
============================================================ */

.page {
    width: min(1180px, 94%);

    margin: 28px auto 50px;
}


/* ============================================================
   PAGE TITLE
============================================================ */

.page-title {
    margin-bottom: 22px;
}


.page-title h1 {
    margin: 0;

    font-size: 25px;

    font-weight: 700;

    color: #172033;
}


.page-title p {
    margin: 6px 0 0;

    font-size: 13px;

    color: #697386;
}


/* ============================================================
   CARDS
============================================================ */

.card {
    background: #ffffff;

    border: 1px solid #dfe3e8;

    border-radius: 8px;

    margin-bottom: 20px;

    overflow: hidden;
}


.card-header {
    min-height: 52px;

    display: flex;

    align-items: center;

    justify-content: space-between;

    padding: 0 20px;

    border-bottom: 1px solid #e8ebef;
}


.card-title {
    font-size: 13px;

    font-weight: 700;

    color: #253247;

    text-transform: uppercase;

    letter-spacing: .045em;
}


.card-note {
    font-size: 11px;

    color: #8a93a1;
}


/* ============================================================
   EMPLOYEE REQUEST
============================================================ */

.request-body {
    padding: 20px;
}


.form-row {
    display: grid;

    grid-template-columns:
        220px
        1fr;

    gap: 18px;

    margin-bottom: 14px;

    align-items: center;
}


.form-label {
    font-size: 12px;

    color: #6b7280;

    font-weight: 600;
}


.form-input {
    width: 100%;

    padding: 10px 12px;

    border: 1px solid #d3d8df;

    border-radius: 5px;

    outline: none;

    font-family: inherit;

    font-size: 13px;

    color: #273244;
}


.form-input:focus,
.issue-input:focus {
    border-color: #5276a4;

    box-shadow:
        0 0 0 2px
        rgba(82, 118, 164, .10);
}


.issue-input {
    min-height: 76px;

    resize: vertical;
}


/* ============================================================
   AGENT ANALYSIS
============================================================ */

.analysis-body {
    padding: 20px;
}


.analysis-grid {
    display: grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap: 10px;

    margin-bottom: 20px;
}


.analysis-item {
    border: 1px solid #e1e5ea;

    background: #fafbfc;

    border-radius: 6px;

    padding: 12px;
}


.analysis-label {
    font-size: 10px;

    text-transform: uppercase;

    letter-spacing: .05em;

    color: #8a93a1;

    margin-bottom: 5px;
}


.analysis-value {
    font-size: 13px;

    font-weight: 700;

    color: #263449;

    word-break: break-word;
}


.status-badge {
    display: inline-block;

    padding: 4px 8px;

    border-radius: 4px;

    font-size: 10px;

    font-weight: 700;
}


.status-resolved {
    background: #edf8f0;

    color: #277844;
}


.status-escalated {
    background: #fff0ef;

    color: #b42318;
}


.resolution-box {
    border: 1px solid #e1e5ea;

    border-radius: 6px;

    overflow: hidden;
}


.resolution-header {
    background: #f7f8fa;

    border-bottom: 1px solid #e1e5ea;

    padding: 10px 13px;

    font-size: 11px;

    font-weight: 700;

    color: #536071;

    text-transform: uppercase;
}


.resolution-content {
    padding: 15px;

    font-size: 13px;

    line-height: 1.7;

    color: #394457;

    white-space: pre-wrap;
}


.source-line {
    margin-top: 12px;

    font-size: 11px;

    color: #778191;
}


.source-line strong {
    color: #344154;
}


/* ============================================================
   TICKET CREATED
============================================================ */

.ticket-created {
    margin-top: 18px;

    border: 1px solid #e6caca;

    background: #fffafa;

    border-radius: 6px;

    padding: 14px;
}


.ticket-created-title {
    font-size: 12px;

    font-weight: 700;

    color: #8f2119;

    margin-bottom: 11px;
}


.ticket-created-grid {
    display: grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap: 9px;
}


.ticket-created-item {
    background: #ffffff;

    border: 1px solid #eadede;

    padding: 9px;

    border-radius: 5px;
}


.ticket-created-item span {
    display: block;

    font-size: 9px;

    color: #9098a4;

    text-transform: uppercase;

    margin-bottom: 4px;
}


.ticket-created-item strong {
    font-size: 11px;

    color: #343d4b;
}


/* ============================================================
   TICKET QUEUE
============================================================ */

.table-wrapper {
    overflow-x: auto;
}


table {
    width: 100%;

    border-collapse: collapse;

    min-width: 760px;
}


thead {
    background: #f5f6f8;
}


th {
    text-align: left;

    padding: 11px 14px;

    border-bottom: 1px solid #dfe3e8;

    font-size: 10px;

    text-transform: uppercase;

    letter-spacing: .045em;

    color: #6f7886;
}


td {
    padding: 13px 14px;

    border-bottom: 1px solid #edf0f3;

    font-size: 12px;

    color: #3b4554;
}


tbody tr:hover {
    background: #fafbfd;
}


.ticket-id {
    font-weight: 700;

    color: #315d8c;
}


.table-status {
    display: inline-block;

    font-size: 10px;

    line-height: 1.35;

    padding: 4px 7px;

    border-radius: 4px;

    background: #f2f4f7;

    color: #586273;
}


/* ============================================================
   CHAT
============================================================ */

.chat-card {
    margin-top: 20px;
}


.chat-area {
    padding: 20px;

    background: #fafbfc;

    max-height: 430px;

    overflow-y: auto;
}


.chat-row {
    display: flex;

    margin-bottom: 18px;
}


.chat-row.user {
    justify-content: flex-end;
}


.chat-wrapper {
    max-width: 72%;
}


.chat-bubble {
    padding: 11px 14px;

    border-radius: 7px;

    font-size: 13px;

    line-height: 1.6;

    white-space: pre-wrap;
}


.chat-bubble.agent {
    background: #ffffff;

    border: 1px solid #dfe3e8;

    color: #3d4654;
}


.chat-bubble.user {
    background: #17365d;

    color: #ffffff;
}


.chat-meta {
    margin-top: 5px;

    font-size: 9px;

    color: #929aa6;
}


.chat-row.user .chat-meta {
    text-align: right;
}


.chat-input-area {
    padding: 14px;

    background: #ffffff;

    border-top: 1px solid #e1e5ea;
}


.chat-input-row {
    display: flex;

    gap: 9px;

    align-items: flex-end;
}


.chat-input {
    flex: 1;

    min-height: 44px;

    max-height: 120px;

    resize: vertical;

    padding: 11px 12px;

    border: 1px solid #ccd2da;

    border-radius: 5px;

    font-family: inherit;

    font-size: 13px;

    outline: none;
}


.send-button {
    height: 44px;

    padding: 0 20px;

    border: 0;

    border-radius: 5px;

    background: #17365d;

    color: #ffffff;

    font-size: 12px;

    font-weight: 700;

    cursor: pointer;
}


.send-button:hover {
    background: #102b4c;
}


.send-button:disabled {
    opacity: .55;

    cursor: not-allowed;
}


.chat-footer {
    display: flex;

    justify-content: space-between;

    align-items: center;

    margin-top: 8px;
}


.security-note {
    font-size: 9px;

    color: #929aa6;
}


.new-request {
    border: 0;

    background: transparent;

    color: #315d8c;

    font-size: 10px;

    font-weight: 700;

    cursor: pointer;
}


.typing {
    display: none;

    padding: 0 0 10px;

    font-size: 10px;

    color: #929aa6;
}


.typing.show {
    display: block;
}


/* ============================================================
   FOOTER
============================================================ */

.footer {
    text-align: center;

    padding: 10px;

    font-size: 10px;

    color: #9aa1ab;
}


/* ============================================================
   MOBILE
============================================================ */

@media (max-width: 800px) {

    .header {
        padding: 0 18px;
    }

    .period {
        display: none;
    }

    .page {
        width: 94%;
    }

    .analysis-grid {
        grid-template-columns:
            repeat(2, 1fr);
    }

    .ticket-created-grid {
        grid-template-columns:
            repeat(2, 1fr);
    }

    .form-row {
        grid-template-columns: 1fr;

        gap: 6px;
    }

    .chat-wrapper {
        max-width: 88%;
    }

}


@media (max-width: 500px) {

    .company-subtitle {
        display: none;
    }

    .header-right {
        display: none;
    }

    .analysis-grid {
        grid-template-columns: 1fr;
    }

    .ticket-created-grid {
        grid-template-columns: 1fr;
    }

}

</style>

</head>


<body>


<!-- ============================================================
     HEADER
============================================================ -->

<header class="header">

    <div class="logo-area">

        <div class="logo">
            VC
        </div>

        <div>

            <div class="company">
                Veridian Corp
            </div>

            <div class="company-subtitle">
                Internal Technology Services
            </div>

        </div>

    </div>


    <div class="header-right">

        <div class="period">
            Assignment 2 · Internal Service Agent
        </div>

        <div class="online">

            <span class="online-dot"></span>

            Agent Online

        </div>

    </div>

</header>



<main class="page">


<!-- ============================================================
     TITLE
============================================================ -->

<section class="page-title">

    <h1>
        IT Service Desk
    </h1>

    <p>
        Employee support requests, agent decisions, approved policies,
        and ticket routing.
    </p>

</section>



<!-- ============================================================
     EMPLOYEE REQUEST
============================================================ -->

<section class="card">

    <div class="card-header">

        <div class="card-title">
            Employee Request
        </div>

        <div class="card-note">
            Current request
        </div>

    </div>


    <div class="request-body">

        <div class="form-row">

            <div class="form-label">
                Employee
            </div>

            <input
                id="employeeName"
                class="form-input"
                placeholder="Enter employee name"
            >

        </div>


        <div class="form-row">

            <div class="form-label">
                Request / Issue
            </div>

            <textarea
                id="requestPreview"
                class="form-input issue-input"
                placeholder="Describe the employee's IT issue..."
            ></textarea>

        </div>

    </div>

</section>



<!-- ============================================================
     AGENT ANALYSIS
============================================================ -->

<section class="card">

    <div class="card-header">

        <div class="card-title">
            Agent Analysis
        </div>

        <div
            id="analysisStatus"
            class="card-note"
        >
            Waiting for request
        </div>

    </div>


    <div
        id="analysisBody"
        class="analysis-body"
    >

        <div class="analysis-grid">

            <div class="analysis-item">

                <div class="analysis-label">
                    Status
                </div>

                <div
                    id="statusValue"
                    class="analysis-value"
                >
                    —
                </div>

            </div>


            <div class="analysis-item">

                <div class="analysis-label">
                    Category
                </div>

                <div
                    id="categoryValue"
                    class="analysis-value"
                >
                    —
                </div>

            </div>


            <div class="analysis-item">

                <div class="analysis-label">
                    Source
                </div>

                <div
                    id="sourceValue"
                    class="analysis-value"
                >
                    —
                </div>

            </div>


            <div class="analysis-item">

                <div class="analysis-label">
                    Ticket
                </div>

                <div
                    id="ticketValue"
                    class="analysis-value"
                >
                    —
                </div>

            </div>

        </div>


        <div class="resolution-box">

            <div class="resolution-header">
                Agent Resolution / Decision
            </div>

            <div
                id="resolutionValue"
                class="resolution-content"
            >
                Submit an employee request below to begin analysis.
            </div>

        </div>


        <div class="source-line">

            <strong>Approved Source:</strong>

            <span id="sourcePath">
                —
            </span>

        </div>


        <div
            id="ticketCreated"
            class="ticket-created"
            style="display:none;"
        >

            <div class="ticket-created-title">
                Support Ticket Created
            </div>


            <div class="ticket-created-grid">

                <div class="ticket-created-item">

                    <span>
                        Ticket ID
                    </span>

                    <strong id="createdTicketId">
                        —
                    </strong>

                </div>


                <div class="ticket-created-item">

                    <span>
                        Status
                    </span>

                    <strong id="createdTicketStatus">
                        —
                    </strong>

                </div>


                <div class="ticket-created-item">

                    <span>
                        Priority
                    </span>

                    <strong id="createdTicketPriority">
                        —
                    </strong>

                </div>


                <div class="ticket-created-item">

                    <span>
                        Reason
                    </span>

                    <strong id="createdTicketReason">
                        —
                    </strong>

                </div>

            </div>

        </div>

    </div>

</section>



<!-- ============================================================
     TICKET QUEUE
============================================================ -->

<section class="card">

    <div class="card-header">

        <div class="card-title">
            Ticket Queue
        </div>

        <div class="card-note">
            Existing IT service records
        </div>

    </div>


    <div class="table-wrapper">

        <table>

            <thead>

                <tr>

                    <th>
                        Ticket ID
                    </th>

                    <th>
                        Employee
                    </th>

                    <th>
                        Issue Summary
                    </th>

                    <th>
                        Status
                    </th>

                </tr>

            </thead>


            <tbody id="ticketTable">

                __TICKET_ROWS__

            </tbody>

        </table>

    </div>

</section>



<!-- ============================================================
     CHAT
============================================================ -->

<section class="card chat-card">

    <div class="card-header">

        <div class="card-title">
            Service Desk Conversation
        </div>

        <div class="card-note">
            Secure internal support channel
        </div>

    </div>


    <div
        id="chatArea"
        class="chat-area"
    >

        <div class="chat-row">

            <div class="chat-wrapper">

                <div class="chat-bubble agent">

                    Hello. I'm the Veridian Corp IT Service Desk agent.
                    Describe the employee's issue and I will check the
                    approved internal procedures, provide guidance, or
                    route the request to IT support when required.

                </div>

                <div class="chat-meta">
                    IT Service Desk · Now
                </div>

            </div>

        </div>

    </div>


    <div class="chat-input-area">


        <div
            id="typing"
            class="typing"
        >
            Agent is reviewing the approved knowledge base...
        </div>


        <div class="chat-input-row">

            <textarea
                id="messageInput"
                class="chat-input"
                placeholder="Describe an IT issue..."
                rows="1"
            ></textarea>


            <button
                id="sendButton"
                class="send-button"
                onclick="sendMessage()"
            >
                Send
            </button>

        </div>


        <div class="chat-footer">

            <div class="security-note">
                Do not share passwords, MFA codes, or other credentials.
            </div>


            <button
                class="new-request"
                onclick="newRequest()"
            >
                New Request
            </button>

        </div>

    </div>

</section>



<div class="footer">
    Veridian Corp · Internal IT Service Desk · Assignment 2 Prototype
</div>


</main>



<script>


const messageInput =
    document.getElementById("messageInput");

const sendButton =
    document.getElementById("sendButton");

const chatArea =
    document.getElementById("chatArea");

const typing =
    document.getElementById("typing");

const employeeName =
    document.getElementById("employeeName");

const requestPreview =
    document.getElementById("requestPreview");


/* ============================================================
   TIME
============================================================ */

function currentTime() {

    return new Date().toLocaleTimeString(
        [],
        {
            hour: "2-digit",
            minute: "2-digit"
        }
    );

}


/* ============================================================
   ESCAPE HTML
============================================================ */

function escapeHtml(value) {

    return String(value ?? "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");

}


/* ============================================================
   CHAT MESSAGE
============================================================ */

function addChatMessage(
    text,
    type,
    data = null
) {

    const row =
        document.createElement("div");

    row.className =
        "chat-row " +
        (type === "user" ? "user" : "");


    const wrapper =
        document.createElement("div");

    wrapper.className =
        "chat-wrapper";


    const bubble =
        document.createElement("div");

    bubble.className =
        "chat-bubble " +
        (type === "user" ? "user" : "agent");


    bubble.textContent =
        text;


    const meta =
        document.createElement("div");

    meta.className =
        "chat-meta";


    meta.textContent =
        (type === "user"
            ? (employeeName.value.trim() || "Employee")
            : "IT Service Desk")
        + " · "
        + currentTime();


    wrapper.appendChild(bubble);

    wrapper.appendChild(meta);


    /* Show ticket inside chat */

    if (
        type === "agent" &&
        data &&
        data.status === "ESCALATED"
    ) {

        const ticket =
            data.ticket || {};


        const ticketBox =
            document.createElement("div");

        ticketBox.style.marginTop =
            "10px";

        ticketBox.style.padding =
            "11px";

        ticketBox.style.background =
            "#fffafa";

        ticketBox.style.border =
            "1px solid #ead5d5";

        ticketBox.style.borderRadius =
            "6px";


        ticketBox.innerHTML = `

            <strong style="
                font-size:11px;
                color:#8f2119;
            ">
                Support ticket created
            </strong>

            <div style="
                margin-top:7px;
                font-size:10px;
                line-height:1.6;
                color:#596273;
            ">

                Ticket ID:
                <strong>
                    ${escapeHtml(
                        data.ticket_id ||
                        ticket.ticket_id ||
                        "Created"
                    )}
                </strong>
                <br>

                Category:
                <strong>
                    ${escapeHtml(
                        data.category ||
                        ticket.category ||
                        "IT"
                    )}
                </strong>
                <br>

                Priority:
                <strong>
                    ${escapeHtml(
                        ticket.priority ||
                        "MEDIUM"
                    )}
                </strong>

            </div>
        `;


        wrapper.appendChild(ticketBox);

    }


    row.appendChild(wrapper);

    chatArea.appendChild(row);

    chatArea.scrollTop =
        chatArea.scrollHeight;

}


/* ============================================================
   UPDATE ANALYSIS PANEL
============================================================ */

function updateAnalysis(data) {

    const status =
        data.status || "—";

    const category =
        data.category || "—";

    const source =
        data.source || "—";

    const sourcePath =
        data.source_path || "—";


    document.getElementById(
        "statusValue"
    ).innerHTML =
        status === "ESCALATED"
            ? '<span class="status-badge status-escalated">ESCALATED</span>'
            : status === "RESOLVED_GUIDANCE"
                ? '<span class="status-badge status-resolved">RESOLVED GUIDANCE</span>'
                : escapeHtml(status);


    document.getElementById(
        "categoryValue"
    ).textContent =
        category;


    document.getElementById(
        "sourceValue"
    ).textContent =
        source;


    document.getElementById(
        "sourcePath"
    ).textContent =
        sourcePath;


    const ticket =
        data.ticket || {};


    document.getElementById(
        "ticketValue"
    ).textContent =
        data.ticket_id ||
        ticket.ticket_id ||
        "Not created";


    document.getElementById(
        "resolutionValue"
    ).textContent =
        data.resolution ||
        data.message ||
        "No response received.";


    document.getElementById(
        "analysisStatus"
    ).textContent =
        status;


    /* Ticket panel */

    const ticketCreated =
        document.getElementById(
            "ticketCreated"
        );


    if (
        status === "ESCALATED" &&
        (
            data.ticket_id ||
            ticket.ticket_id
        )
    ) {

        ticketCreated.style.display =
            "block";


        document.getElementById(
            "createdTicketId"
        ).textContent =
            data.ticket_id ||
            ticket.ticket_id ||
            "Created";


        document.getElementById(
            "createdTicketStatus"
        ).textContent =
            ticket.status ||
            "ESCALATED";


        document.getElementById(
            "createdTicketPriority"
        ).textContent =
            ticket.priority ||
            "MEDIUM";


        document.getElementById(
            "createdTicketReason"
        ).textContent =
            ticket.reason ||
            "Escalated to IT support";

    }
    else {

        ticketCreated.style.display =
            "none";

    }

}


/* ============================================================
   SEND MESSAGE
============================================================ */

async function sendMessage() {

    const message =
        messageInput.value.trim();


    if (!message) {

        messageInput.focus();

        return;

    }


    /* Show employee request */

    requestPreview.value =
        message;


    addChatMessage(
        message,
        "user"
    );


    messageInput.value = "";

    messageInput.style.height =
        "44px";


    sendButton.disabled =
        true;


    typing.classList.add(
        "show"
    );


    try {

        const response =
            await fetch(
                "/support",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        message: message
                    })
                }
            );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail ||
                "Request failed"
            );

        }


        typing.classList.remove(
            "show"
        );


        updateAnalysis(data);


        addChatMessage(

            data.resolution ||
            data.message ||
            "No response received.",

            "agent",

            data

        );


    }
    catch (error) {

        typing.classList.remove(
            "show"
        );


        document.getElementById(
            "resolutionValue"
        ).textContent =
            "Unable to process the request. Please try again.";


        addChatMessage(
            "Unable to process the request right now. Please try again.",
            "agent"
        );


        console.error(error);

    }


    sendButton.disabled =
        false;


    messageInput.focus();

}


/* ============================================================
   NEW REQUEST
============================================================ */

function newRequest() {

    employeeName.value = "";

    requestPreview.value = "";

    messageInput.value = "";


    document.getElementById(
        "statusValue"
    ).textContent = "—";


    document.getElementById(
        "categoryValue"
    ).textContent = "—";


    document.getElementById(
        "sourceValue"
    ).textContent = "—";


    document.getElementById(
        "ticketValue"
    ).textContent = "—";


    document.getElementById(
        "sourcePath"
    ).textContent = "—";


    document.getElementById(
        "resolutionValue"
    ).textContent =
        "Submit an employee request below to begin analysis.";


    document.getElementById(
        "analysisStatus"
    ).textContent =
        "Waiting for request";


    document.getElementById(
        "ticketCreated"
    ).style.display =
        "none";


    chatArea.innerHTML = `

        <div class="chat-row">

            <div class="chat-wrapper">

                <div class="chat-bubble agent">

                    Hello. I'm the Veridian Corp IT Service Desk agent.
                    Describe the employee's issue and I will check the
                    approved internal procedures, provide guidance, or
                    route the request to IT support when required.

                </div>

                <div class="chat-meta">
                    IT Service Desk · Now
                </div>

            </div>

        </div>

    `;


    messageInput.focus();

}


/* ============================================================
   ENTER TO SEND
============================================================ */

messageInput.addEventListener(
    "keydown",
    function(event) {

        if (
            event.key === "Enter" &&
            !event.shiftKey
        ) {

            event.preventDefault();

            sendMessage();

        }

    }
);


/* ============================================================
   AUTO RESIZE
============================================================ */

messageInput.addEventListener(
    "input",
    function() {

        this.style.height =
            "44px";

        this.style.height =
            Math.min(
                this.scrollHeight,
                120
            ) + "px";

    }
);


</script>


</body>
</html>
"""


# ============================================================
# BUILD TICKET TABLE
# ============================================================

def build_ticket_rows():

    rows = ""

    for ticket in TICKET_QUEUE:

        rows += f"""
        <tr>

            <td>
                <span class="ticket-id">
                    {ticket["id"]}
                </span>
            </td>

            <td>
                {ticket["employee"]}
            </td>

            <td>
                {ticket["issue"]}
            </td>

            <td>
                <span class="table-status">
                    {ticket["status"]}
                </span>
            </td>

        </tr>
        """

    return rows


HTML_PAGE = HTML_PAGE.replace(
    "__TICKET_ROWS__",
    build_ticket_rows()
)


# ============================================================
# ROUTES
# ============================================================

@app.get("/", response_class=HTMLResponse)
def home():
    return HTML_PAGE


@app.post("/support")
def support(request: EmployeeRequest):
    return run_agent(request.message)