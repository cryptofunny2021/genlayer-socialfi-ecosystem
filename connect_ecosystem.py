# connect_ecosystem.py
# اتصال هوشمند قراردادها در GenLayer SocialFi Ecosystem

from genlayer import *

# آدرس‌های ثابت قراردادها
CONTRACTS = {
    "interaction_hub": Address("0xF4f25C67D8aaa24A71E85C9cCF61c5c1a8F2f8b1"),
    "reputation": Address("0x58a73d1dC168B4BAdf5965758656d37d963e4a81"),
    "token": Address("0xeA166C0845904c919A5CD501465976B8d03dBfE6"),
    "task": Address("0x8d5359CCB96900Fde7fF94321a74188299984208"),
    "dispute": Address("0x4DEC89Af46EaB9cc54DDd6BCB037B3D16B97eb58")
}

def main():
    print("🔗 GenLayer SocialFi Ecosystem Connector")
    print("ثبت یک تعامل تست...\n")
    
    try:
        hub = gl.contract(CONTRACTS["interaction_hub"])
        hub.record_interaction()
        print("✅ تعامل با موفقیت ثبت شد!")
        print("   → Reputation و Token باید اتوماتیک آپدیت شده باشند.")
    except Exception as e:
        print("❌ خطا:", e)

if __name__ == "__main__":
    main()
