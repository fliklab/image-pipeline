def process(input_dict):
    num = input_dict.get("config", {}).get("num", 5)
    run_id = input_dict["run_id"]
    news_items = [{"title": f"Mock News {i}", "content": f"Content {i}."} for i in range(num)]
    return {"news_items": news_items, "run_id": run_id}
