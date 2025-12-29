import os
import shutil

# Setup
target_folder = "assets"
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# Mapping your exact filenames to professional resume-ready names
mapping = {
    # Forensic Samples (Selecting the best ELA/Original comparisons)
    "WhatsApp Image 2025-11-14 at 20.41.21_e1635a9d (1).jpg": "ela_sample_1.jpg",
    "WhatsApp Image 2025-11-14 at 20.41.21_fdb377a0 (1).jpg": "ela_sample_2.jpg",
    
    # Model Architectures
    "The-architecture-of-the-MobileNetv2-network.png": "mobilenetv2_architecture.png",
    
    # Comparative Results (EliteNet vs MobileNetV2)
    "cm_elite.png": "confusion_matrix_elitenet.png",
    "cm_mv2.png": "confusion_matrix_mobilenetv2.png",
    "val_curve.png": "training_validation_curves.png"
}

def finalize_project():
    print("🚀 Finalizing ForgeryLens Assets...")
    count = 0
    for old, new in mapping.items():
        if os.path.exists(old):
            shutil.move(old, os.path.join(target_folder, new))
            print(f"✅ Moved & Renamed: {old} -> {target_folder}/{new}")
            count += 1
    print(f"\n✨ Done! {count} essential images are now in /assets.")

if __name__ == "__main__":
    finalize_project()