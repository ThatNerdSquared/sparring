//
//  ContentView.swift
//  Landmarks
//
//  Created by Nathan Yeung on 2022-06-04.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        LandmarkList()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
            .environmentObject(ModelData())
            .previewDevice("iPhone 13")
    }
}
