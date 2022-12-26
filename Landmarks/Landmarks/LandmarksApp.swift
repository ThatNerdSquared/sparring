//
//  LandmarksApp.swift
//  Landmarks
//
//  Created by Nathan Yeung on 2022-06-04.
//

import SwiftUI

@main
struct LandmarksApp: App {
    @State private var modelData = ModelData()
    
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(modelData)
        }
    }
}
