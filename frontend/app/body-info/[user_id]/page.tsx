import BodyInfoForm from "./BodyInfoForm";

export default async function BodyInfoPage() {
    const res = await fetch(
        "http://localhost:8000/get_body_info/1", // "http://localhost:8000/get_body_info/${user_id}"の記述は後日対応。一旦user_id=1でハードコーディングしておく
        { cache: "no-store" }
    );

    const bodyInfo = await res.json()

    return (
        <div className="container-app">
            <h1 className="text-2xl font-bold mb-6">身体情報</h1>

            <div className="card">
                <div className="kpi">
                    <div className="kpi-label">身長</div>
                    <div className="kpi-value">{bodyInfo.height} cm</div>
                </div>
            </div>

            <div className="card mt-3">
                <div className="kpi">
                    <div className="kpi-label">体重</div>
                    <div className="kpi-value">{bodyInfo.weight} kg</div>
                </div>
            </div>

            <div className="card mt-3">
                <div className="kpi">
                    <div className="kpi-label">生活レベル</div>
                    <div className="kpi-value">{bodyInfo.activity_status}</div>
                </div>
            </div>
            {/* 登録フォームを表示 */}
            <BodyInfoForm />
        </div>
    )
}