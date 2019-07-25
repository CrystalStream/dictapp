html = """
<div class="tlid-source-target main-header">
   <div class="source-target-row">
      <div class="tlid-input input">
         <div class="tlid-language-bar ls-wrap">
            <div class="sl-wrap">
               <div class="sl-sugg">
                  <div class="ls-left-arrow"></div>
                  <div class="sl-sugg-button-container">
                     <div role="button" class="goog-inline-block jfk-button jfk-button-standard jfk-button-collapse-right" tabindex="0" aria-pressed="false" value="auto" style="user-select: none;">Detect language</div>
                     <div role="button" class="goog-inline-block jfk-button jfk-button-standard jfk-button-collapse-left jfk-button-collapse-right" tabindex="0" aria-pressed="false" value="en" id="sugg-item-es" style="user-select: none;">English</div>
                     <div role="button" class="goog-inline-block jfk-button jfk-button-standard jfk-button-collapse-left jfk-button-collapse-right jfk-button-checked" tabindex="0" aria-pressed="true" value="es" id="sugg-item-en" style="user-select: none;">Spanish</div>
                     <div role="button" class="goog-inline-block jfk-button jfk-button-standard jfk-button-collapse-left jfk-button-collapse-right" tabindex="0" aria-pressed="false" value="fr" id="sugg-item-fr" style="user-select: none;">French</div>
                  </div>
                  <div class="ls-right-arrow"></div>
               </div>
               <div class="sugg-fade"></div>
               <div class="sl-more tlid-open-source-language-list" aria-label="More" role="button" tabindex="0"></div>
            </div>
            <div class="sl-selector lang_list">
               <div class="lang-btn"><a class="ls-select new-ls-select sl-button tlid-open-small-source-language-list" aria-label="Spanish" tabindex="0">Spanish</a></div>
            </div>
            <div class="swap-wrap">
               <div class="swap jfk-button-narrow jfk-button-standard jfk-button" aria-label="Swap languages (Cmd+Shift+S)" role="button" data-tooltip="Swap languages (Cmd+Shift+S)" data-tooltip-align="b,c" style="user-select: none;" aria-disabled="false" tabindex="0">
                  <div class="jfk-button-img"></div>
               </div>
            </div>
            <div class="tl-wrap">
               <div class="tl-sugg">
                  <div class="ls-left-arrow"></div>
                  <div class="sl-sugg-button-container">
                     <div role="button" class="goog-inline-block jfk-button jfk-button-standard jfk-button-collapse-right" tabindex="0" aria-pressed="false" value="es" id="sugg-item-en" style="user-select: none;">Spanish</div>
                     <div role="button" class="goog-inline-block jfk-button jfk-button-standard jfk-button-collapse-left jfk-button-collapse-right jfk-button-checked" tabindex="0" aria-pressed="true" value="en" id="sugg-item-es" style="user-select: none;">English</div>
                     <div role="button" class="goog-inline-block jfk-button jfk-button-standard jfk-button-collapse-left jfk-button-collapse-right" tabindex="0" aria-pressed="false" value="pt" id="sugg-item-pt" style="user-select: none;">Portuguese</div>
                  </div>
                  <div class="ls-right-arrow"></div>
               </div>
               <div class="sugg-fade"></div>
               <div class="tl-more tlid-open-target-language-list" aria-label="More" role="button" tabindex="0"></div>
            </div>
            <div class="tl-selector lang_list">
               <div class="lang-btn"><a class="ls-select new-ls-select tl-button tlid-open-small-target-language-list" aria-label="English" tabindex="0">English</a></div>
            </div>
         </div>
         <div class="source-wrap">
            <div class="input-full-height-wrapper tlid-input-full-height-wrapper">
               <div class="source-input">
                  <div id="input-wrap" class="tlid-input-area input-area less-padding">
                     <div class="gt-hl-layer" dir="" style="box-sizing: content-box; left: 0px; top: 0px; direction: ltr;"></div>
                     <textarea id="source" class="orig tlid-source-text-input goog-textarea" rows="1" spellcheck="false" autocapitalize="off" autocomplete="off" autocorrect="off" style="overflow: auto hidden; box-sizing: border-box; height: 70px; direction: ltr; padding-bottom: 18px;"></textarea>
                     <div class="text-dummy">Coches</div>
                     <div id="gt-src-is" style="display: none; user-select: none; direction: ltr; text-align: left;" class="gt-is-mobile gt-is" role="menu">
                        <div id="gt-src-is-list" class="gt-is-ctr" style="user-select: none;"></div>
                     </div>
                  </div>
                  <div class="source-header">
                     <div class="clear-wrap">
                        <div class="clear jfk-button-flat tlid-clear-source-text jfk-button" aria-label="Clear text" data-tooltip="Clear text" role="button" aria-hidden="false" data-tooltip-align="t,c" style="user-select: none;" tabindex="0">
                           <div class="jfk-button-img"></div>
                        </div>
                     </div>
                  </div>
                  <div class="tlid-source-transliteration-container source-transliteration-container transliteration-container">
                     <div class="tlid-transliteration-content transliteration-content full"></div>
                     <div class="tlid-show-more-link truncate-link" style="display:none">Show more</div>
                     <div class="tlid-show-less-link truncate-link" style="display:none">Show less</div>
                  </div>
                  <div id="spelling-correction" class="tlid-spelling-correction spelling-correction gt-spell-correct-message" style="display: none;">
                     Translate from: <a href="javascript:void(0)" style="direction: ltr; text-decoration: none;">Spanish</a>
                     <div class="gt-spell-icon"></div>
                  </div>
                  <div class="source-footer-wrap source-or-target-footer">
                     <div class="source-input-tools" id="gt-input-tool">
                        <div>
                           <span class="ita-kd-inputtools-div">
                              <div class="goog-container goog-container-vertical" tabindex="-1" style="user-select: none;"><a class="ita-kd-icon-button ita-kd-inputtool-icon ita-kd-small ita-kd-left" tabindex="0" style="user-select: none;" data-tooltip="Turn on Virtual Keyboard" aria-label="Turn on Virtual Keyboard" data-tooltip-align="t,c"><span class="ita-kd-img ita-kd-icon ita-kd-icon-span ita-icon-0" style="user-select: none;"></span></a><a class="ita-kd-icon-button ita-kd-dropdown ita-kd-right" tabindex="0" style="user-select: none;" data-tooltip="Select Input Tool" aria-label="Select Input Tool" data-tooltip-align="t,c"><span class="ita-kd-img ita-kd-arrow ita-kd-icon-span" style="user-select: none;"></span></a></div>
                           </span>
                        </div>
                     </div>
                     <div class="character-count tlid-character-count">
                        <div class="cc-ctr normal">6/5000</div>
                        <div class="cc-msg" style="display: none;"></div>
                     </div>
                     <div class="source-footer">
                        <div class="speech-wrap source-or-target-footer-button left-positioned">
                           <span class="speech-border"></span><span class="speech-border speech-background"></span>
                           <div id="gt-speech" class="speech-button goog-toolbar-button" aria-label="Turn on voice input" data-tooltip-align="t,c" aria-pressed="false" role="button" aria-disabled="false" tabindex="0" style="user-select: none;" data-tooltip="Turn on voice input">
                              <span class="jfk-button-img"></span>
                              <div class="jfk-bubble" role="alertdialog" aria-describedby="bubble-3" style="display: none;">
                                 <div class="jfk-bubble-content-id" id="bubble-3">
                                    <div>
                                       <div class="speech-mic">
                                          <div class="gt-speech-l1"></div>
                                          <div class="gt-speech-l2"></div>
                                          <div class="gt-speech-l3"></div>
                                          <div class="gt-speech-l4"></div>
                                       </div>
                                       <div class="speech-mic-label">Speak Now</div>
                                    </div>
                                 </div>
                                 <div class="jfk-bubble-arrow-id jfk-bubble-arrow">
                                    <div class="jfk-bubble-arrowimplbefore"></div>
                                    <div class="jfk-bubble-arrowimplafter"></div>
                                 </div>
                              </div>
                           </div>
                        </div>
                        <div class="src-tts left-positioned ttsbutton jfk-button-flat source-or-target-footer-button jfk-button" aria-label="Listen" data-tooltip="Listen" aria-pressed="false" role="button" data-tooltip-align="t,c" aria-hidden="false" aria-disabled="false" style="user-select: none;" tabindex="0">
                           <div class="jfk-button-img"></div>
                        </div>
                     </div>
                  </div>
               </div>
            </div>
         </div>
         <div id="gt-ovfl" style="display: none;" class="snck ovfl">
            <div id="gt-ovfl-ctr" class="ovfl-ctr"><span id="gt-ovfl-msg" class="snck-msg" role="alert" aria-live="alert"></span><span id="gt-ovfl-xlt" class="ovfl-xlt goog-button" role="button" tabindex="0" style="user-select: none;">TRANSLATE MORE</span></div>
         </div>
         <div id="gt-ntfcn" style="display: none;" class="snck ntfcn">
            <div id="gt-ntfcn-ctr" class="ntfcn-ctr"><span id="gt-ntfcn-msg" class="snck-msg" role="alert" aria-live="alert"></span></div>
         </div>
         <div id="gt-cmty" style="display: none;" class="snck cmty">
            <div id="gt-cmty-ctr" class="cmty-ctr"><span id="gt-cmty-msg" class="snck-msg" role="alert" aria-live="alert">Translation verified by Translate Community</span><span id="gt-cmty-btn" class="cmty-btn goog-button" role="button" tabindex="0" style="user-select: none;">Join</span></div>
         </div>
      </div>
      <div class="tlid-results-container results-container">
         <div class="error-placeholder placeholder"><span class="tlid-result-error"></span><span class="tlid-result-container-error-button translation-error-button">Try again</span></div>
         <span class="empty-placeholder placeholder">Translation</span><span class="translating-placeholder placeholder">Translating...</span>
         <div class="gendered-translations-header">Translations are gender-specific. <a class="gendered-translations-learn-more" href="https://support.google.com/translate?p=gendered_translations&amp;hl=en" target="_blank">Learn more</a></div>
         <div class="tlid-result result-dict-wrapper">
            <div class="result tlid-copy-target">
               <div class="result-header">
                  <div class="starbutton jfk-button-flat jfk-button unstarred" aria-label="Star translation" data-tooltip="Star translation" role="button" tabindex="0" data-tooltip-align="t,c" style="user-select: none;">
                     <div class="jfk-button-img"></div>
                  </div>
               </div>
               <div class="text-wrap tlid-copy-target">
                  <div class="result-shield-container tlid-copy-target" tabindex="0"><span class="tlid-translation translation" lang="en"><span title="">Cars</span></span><span class="tlid-translation-gender-indicator translation-gender-indicator"></span><span class="tlid-trans-verified-button trans-verified-button" style="display:none" role="button"></span></div>
               </div>
               <div class="tlid-result-transliteration-container result-transliteration-container transliteration-container">
                  <div class="tlid-transliteration-content transliteration-content full"></div>
                  <div class="tlid-show-more-link truncate-link" style="display:none">Show more</div>
                  <div class="tlid-show-less-link truncate-link" style="display:none">Show less</div>
               </div>
               <div class="result-footer source-or-target-footer tlid-copy-target">
                  <div class="tlid-share-translation-button share-translation-button jfk-button-flat source-or-target-footer-button right-positioned jfk-button" aria-label="Share translation" data-tooltip="Share translation" role="button" style="user-select: none;" tabindex="0" data-tooltip-align="t,c">
                     <div class="jfk-button-img"></div>
                  </div>
                  <div class="tlid-suggest-edit-button suggest-edit-button jfk-button-flat source-or-target-footer-button right-positioned jfk-button" aria-label="Suggest an edit" data-tooltip="Suggest an edit" role="button" style="user-select: none;" tabindex="0" data-tooltip-align="t,c">
                     <div class="jfk-button-img"></div>
                  </div>
                  <div class="more-wrapper">
                     <div class="morebutton jfk-button-flat source-or-target-footer-button tlid-result-footer-more-button right-positioned goog-inline-block goog-menu-button" data-tooltip="More" role="button" aria-expanded="false" style="user-select: none;" tabindex="0" aria-haspopup="true" aria-label="More" data-tooltip-align="t,c">
                        <div class="goog-inline-block goog-menu-button-outer-box">
                           <div class="goog-inline-block goog-menu-button-inner-box">
                              <div class="goog-inline-block goog-menu-button-caption">
                                 <div class="jfk-button-img"></div>
                              </div>
                              <div class="goog-inline-block goog-menu-button-dropdown">&nbsp;</div>
                           </div>
                        </div>
                     </div>
                     <div class="moremenu goog-menu" role="menu" aria-haspopup="true" style="user-select: none; display: none;">
                        <div class="goog-menuitem tlid-suggest-edit-menu-item" role="menuitem" style="user-select: none;" id=":f">
                           <div class="goog-menuitem-content">Suggest an edit</div>
                        </div>
                        <div class="goog-menuitem tlid-share-translation-menu-item" role="menuitem" style="user-select: none;" id=":g">
                           <div class="goog-menuitem-content">Share translation</div>
                        </div>
                     </div>
                  </div>
                  <div class="tlid-copy-translation-button copybutton jfk-button-flat source-or-target-footer-button right-positioned jfk-button" aria-label="Copy translation" data-tooltip="Copy translation" role="button" style="user-select: none;" tabindex="0" data-tooltip-align="t,c">
                     <div class="jfk-button-img"></div>
                  </div>
                  <div class="res-tts ttsbutton-res left-positioned ttsbutton jfk-button-flat source-or-target-footer-button jfk-button" aria-label="Listen" data-tooltip="Listen" aria-pressed="false" role="button" style="user-select: none;" tabindex="0" data-tooltip-align="t,c">
                     <div class="jfk-button-img"></div>
                  </div>
               </div>
            </div>
            <div class="gt-edit" style="display:none">
               <div class="gt-clear clear-button goog-toolbar-button" data-tooltip="Clear text" aria-label="Clear text" data-tooltip-align="t,c" role="button" style="user-select: none; display: none;" aria-hidden="true"><span class="jfk-button-img"></span></div>
               <textarea class="contribute-target goog-textarea" style="overflow: auto hidden; box-sizing: border-box; height: auto; direction: ltr;" rows="1"></textarea>
               <div class="st-wrap" style="display: none;">
                  <div class="st-stp1" style="display: none;">
                     <div id="st-buttons">
                        <div role="button" class="goog-inline-block jfk-button jfk-button-action" tabindex="0" style="user-select: none;">Submit</div>
                        <div role="button" class="goog-inline-block jfk-button jfk-button-standard" tabindex="0" style="user-select: none;">Cancel</div>
                     </div>
                     <div class="st-stp1-epu-text">Your contribution will be used to improve translation quality and may be shown (without identifying you) to other users</div>
                  </div>
               </div>
            </div>
         </div>
      </div>
   </div>
   <div class="tlid-select-file-page-container"></div>
</div>
"""
