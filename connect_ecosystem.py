# connect_ecosystem.py

from genlayer import *
import json

CONTRACTS = {
    "reputation": "0x58a73d1dC168B4BAdf5965758656d37d963e4a81",
    "token": "0xeA166C0845904c919A5CD501465976B8d03dBfE6",
    "interaction_hub": "0xF4f25C67D8aaa24A71E85C9cCF61c5c1a8F2f8b1",
    "task_marketplace": "0x8d5359CCB96900Fde7fF94321a74188299984208",
    "dispute": "0x4DEC89Af46EaB9cc54DDd6BCB037B3D16B97eb58"
}

def main():
    print("🔗 GenLayer SocialFi Ecosystem Connector")
    
    # مثال: ثبت یک تعامل از طریق Hub
    hub = gl.contract(CONTRACTS["interaction_hub"])
    
    print("ثبت تعامل جدید...")
    hub.record_interaction()   # این باید کار کنه اگر قبلاً method وجود داشته باشه
    
    print("✅ تعامل ثبت شد")
    print("Reputation و Token باید اتوماتیک آپدیت بشن")

if __name__ == "__main__":
    main()
