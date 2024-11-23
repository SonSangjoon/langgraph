import uuid

from langchain_core.messages import HumanMessage

from graph import graph


if __name__ == "__main__":
    config = {"configurable": {"thread_id": str(uuid.uuid4())}}
    while True:
        user = input("User (q/Q to quit): ")
        print(f"User (q/Q to quit): {user}")
        if user in {"q", "Q"}:
            print("AI: Byebye")
            break
        output = None
        for output in graph.stream(
            {"messages": [HumanMessage(content=user)]},
            config=config,
            stream_mode="updates",
        ):
            last_message = next(iter(output.values()))["messages"][-1]
            last_message.pretty_print()

        if output and "prompt" in output:
            print("Done!")
