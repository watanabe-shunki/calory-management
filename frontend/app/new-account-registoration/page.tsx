"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function NewAccountRegistrationPage() {
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState("");
    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
       
        try {    
            const res = await fetch("http://localhost:8000/create_user", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    "name": name,
                    "email": email,
                    "password": password
                })
            });

            if (!res.ok) {
                console.error("登録失敗" + res.status);
                const text = await res.text();
                console.log("response", text);
                setMessage("登録に失敗しました。");
                return;
            }
            if (res.ok) {
                router.push("/login?message=登録が完了しました。ログインしてください。");
            }
        } catch (error) {
            console.error(error);
            setMessage("登録に失敗しました。");
        }
    };

    return (
        <div>
            <h1>New Account Registration</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="name">Name:</label>
                    <input
                        type="text"
                        id="name"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                    />
                </div>
                <div>
                    <label htmlFor="email">Email:</label>
                    <input
                        type="email"
                        id="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                    />
                </div>
                <div>
                    <label htmlFor="password">Password:</label>
                    <input
                        type="password"
                        id="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </div>
                <button type="submit">Register</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
}