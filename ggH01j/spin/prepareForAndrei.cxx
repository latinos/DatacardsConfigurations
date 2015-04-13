{

 TFile* fileIn  = new TFile("datacards/shapes/hww-19.47fb.mH125.of_0j_shape.root","READ");
 TFile* fileOut = new TFile("spinhww.root","RECREATE");

 TH1F* ggh_sbi = (TH1F*) fileIn->Get("histo_ggH_sbi");
 TH1F* ggh_b   = (TH1F*) fileIn->Get("histo_ggH_b");
 TH1F* ggh_s   = (TH1F*) fileIn->Get("histo_ggH_s");

 TH1F* ggh_i   = (TH1F*) ggh_sbi->Clone("histo_ggH_i");
 ggh_i->Sumw2();

 ggh_i -> Add (ggh_b,-1);
 ggh_i -> Add (ggh_s,-1);

 ggh_sbi->SetLineColor(kRed);
 ggh_s->SetLineColor(kGreen);
 ggh_b->SetLineColor(kYellow);

 ggh_sbi->Draw();
 ggh_s->Draw("same");
 ggh_b->Draw("same");
 ggh_i->Draw("same");


 ggh_sbi->Write();
 ggh_b->Write();
 ggh_s->Write();
 ggh_i->Write();


 TH1F* qqH_sbi = (TH1F*) fileIn->Get("histo_qqH_sbi");
 TH1F* qqH_b   = (TH1F*) fileIn->Get("histo_qqH_b");
 TH1F* qqH_s   = (TH1F*) fileIn->Get("histo_qqH_s");

 TH1F* qqH_i   = (TH1F*) qqH_sbi->Clone("histo_qqH_i");
 qqH_i->Sumw2();

 qqH_i -> Add (qqH_b,-1);
 qqH_i -> Add (qqH_s,-1);

 qqH_sbi->SetLineColor(kRed);
 qqH_s->SetLineColor(kGreen);
 qqH_b->SetLineColor(kYellow);

 qqH_sbi->Draw();
 qqH_s->Draw("same");
 qqH_b->Draw("same");
 qqH_i->Draw("same");


 qqH_sbi->Write();
 qqH_b->Write();
 qqH_s->Write();
 qqH_i->Write();

}