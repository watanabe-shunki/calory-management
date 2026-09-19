"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

interface FoodsInfoFormProps {
    onSuccess: () => Promise<void>;
}

export default function FoodsInfoFormPage({ onSuccess }: FoodsInfoFormProps) {
    const [foodName, setFoodsName] = useState("");
    const [calories, setCalories] = useState("");
    const [protein, setProtein] = useState("");
    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        const access_token = localStorage.getItem("access_token");
        if (!access_token) {
            console.error("No access token found");
            router.push("/login");
            return;
        }

        const res = await fetch("http://localhost:8000/create_foods_info", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${access_token}`,
            },
            body: JSON.stringify({
                foods_name: foodName,
                calory: Number(calories),
                protein: Number(protein),
            }),
        });
        if (res.status === 401) {
            localStorage.removeItem("access_token");
            router.push("/login");
            return;
        }

        if (!res.ok) {
            console.error("登録失敗" + res.status);
            const text = await res.text();
            console.log("response", text);
            setMessage("登録に失敗しました。");
            return;
        }

        const data = await res.json();
        console.log("登録成功", data);
        setFoodsName("");
        setCalories("");
        setProtein("");
        setMessage("登録が完了しました。");
        await onSuccess();
    };

    const [message, setMessage] = useState("");

    return (
        <div className="container-app">
            <h1 className="text-2xl font-bold mb-4">食品情報登録</h1>
            
            <form onSubmit={handleSubmit}>
                <div>
                    <label>食品名:</label>
                    <input
                        className="input"
                        type="text"
                        value={foodName}
                        onChange={(e) => setFoodsName(e.target.value)}
                />
                </div>
                <div>
                    <label>カロリー:</label>
                    <input
                        className="input"
                        type="number"
                        value={calories}
                        onChange={(e) => setCalories(e.target.value)}
                    />
                </div>
                <div>
                    <label>タンパク質:</label>
                    <input
                        className="input"
                        type="number"
                        step="any"
                        value={protein}
                        onChange={(e) => setProtein(e.target.value)}
                    />
                </div>
                <button type="submit" className="btn btn-primary w-full">
                    登録
                </button>
                {message && (
                    <p className="mt-4 text-center">{message}</p>
                )}
            </form>
        </div>
    );
};