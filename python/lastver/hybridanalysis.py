from hybrid_analysis_api import HybridAnalysis

ha = HybridAnalysis('7ztcs500471ac1a6hpolso1668d509ba6fy839llc53243bdwji92jw76537777d')

ha.search_hash('1d389849db67d50f48d30670e1e8437a97a33fdba75a31e75c06176b1cfb4a21')
ha.search_hashes(['1d389849db67d50f48d30670e1e8437a97a33fdba75a31e75c06176b1cfb4a21',
                  'bd3a86453614b1c1f72685d9393d6cbe63e1097267d12b19340c62870ce53e50'])
ha.search_terms({'filename': 'invoice.exe', 'tag': 'ransomware'})

ha.quick_scan_state()
ha.quick_scan_file('lookup_ha', 'xtgxutpf.js', '../xtgxutpf.js', options={'comment': 'Bondat malware'})
ha.quick_scan_url_to_file('lookup_ha', 'url')
ha.quick_scan_url_for_analysis('all', 'https://www.google.com')
ha.quick_scan_id('scan_id')

ha.overview_sha256('bd3a86453614b1c1f72685d9393d6cbe63e1097267d12b19340c62870ce53e50')
ha.overview_sha256_refresh('bd3a86453614b1c1f72685d9393d6cbe63e1097267d12b19340c62870ce53e50')
ha.overview_sha256_summary('bd3a86453614b1c1f72685d9393d6cbe63e1097267d12b19340c62870ce53e50')
ha.overview_sha256_sample('bd3a86453614b1c1f72685d9393d6cbe63e1097267d12b19340c62870ce53e50')

ha.submit_file(100, 'xtgxutpf.js', '../xtgxutpf.js', options={'comment': 'Bondat malware'})
ha.submit_url_to_file(100, 'url')
ha.submit_url_for_analysis(100, 'https://www.google.com')
ha.submit_hash_for_url('url')
ha.submit_dropped_file('report_id', 'file_hash')

ha.report_id_state('report_id')
ha.report_id_summary('report_id')
ha.report_summary(['report_id_0', 'report_id_1'])
ha.report_id_file_type('report_id', 'xml')
ha.report_id_screenshots('report_id')
ha.report_id_dropped_file_raw_hash('report_id', 'hash_file')
ha.report_id_dropped_files('report_id')

ha.system_version()
ha.system_environments()
ha.system_stats()
ha.system_state()
ha.system_configuration()
ha.system_backend()
ha.system_queue_size()
ha.system_in_progress()
ha.system_total_submissions()
ha.system_heartbeat()

ha.key_current()

ha.feed_latest()
