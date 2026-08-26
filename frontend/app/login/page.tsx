"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function LoginPage() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState("");
    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        const formData = new URLSearchParams();
        formData.append("username", email);
        formData.append("password", password);
        try {
            const res = await fetch(`http://localhost:8000/login`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                body: formData,
            });
            if (!res.ok) {
                if (res.status === 401) {
                    setMessage("メールアドレスまたはパスワードが正しくありません。");
                    return;
                }
                setMessage("ログインに失敗しました。");
                return;
            }
            const data = await res.json();
            localStorage.setItem("access_token", data.access_token);
            router.push("/body-info");
        } catch (error) {
            console.error(error);
            setMessage("ログインに失敗しました。");
        }
    };
    return (
        <div className="container-app">
            <h1 className="text-2xl font-bold mb-6">ログイン画面</h1>
            <form onSubmit={handleSubmit} className="card space-y-4">
                <div>
                    <label>メールアドレス</label>
                    <input
                        type="email"
                        name="email"
                        className="input"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        placeholder="メールアドレス"
                    />
                </div>
                <div>
                    <label>パスワード</label>
                    <input
                        type="password"
                        name="password"
                        className="input"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        placeholder="パスワード"
                    />
                </div>
                <button type="submit" className="btn btn-primary">
                    ログイン
                </button>
                {message && (
                    <p>{message}</p>
                )}
            </form>
        </div>
    );
}