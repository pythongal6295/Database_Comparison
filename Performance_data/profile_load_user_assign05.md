         668078 function calls (660078 primitive calls) in 0.799 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.799    0.799 <string>:1(<module>)
     2000    0.002    0.000    0.015    0.000 __init__.py:1065(_decode_all_selective)
        1    0.000    0.000    0.000    0.000 _bootlocale.py:11(getpreferredencoding)
     2000    0.001    0.000    0.001    0.000 _collections_abc.py:392(__subclasshook__)
    14000    0.003    0.000    0.013    0.000 abc.py:137(__instancecheck__)
     2000    0.001    0.000    0.003    0.000 abc.py:141(__subclasscheck__)
     2000    0.000    0.000    0.000    0.000 binary.py:312(subtype)
     2000    0.000    0.000    0.000    0.000 client_options.py:244(retry_writes)
     2000    0.001    0.000    0.001    0.000 client_session.py:131(__init__)
     2000    0.001    0.000    0.001    0.000 client_session.py:240(_validate_session_write_concern)
     2000    0.001    0.000    0.001    0.000 client_session.py:289(__init__)
    14000    0.005    0.000    0.005    0.000 client_session.py:297(active)
     2000    0.001    0.000    0.001    0.000 client_session.py:300(reset)
     2000    0.002    0.000    0.003    0.000 client_session.py:350(__init__)
     4000    0.002    0.000    0.016    0.000 client_session.py:362(end_session)
     4000    0.003    0.000    0.015    0.000 client_session.py:369(_end_session)
     4000    0.001    0.000    0.001    0.000 client_session.py:378(_check_ended)
     2000    0.000    0.000    0.000    0.000 client_session.py:406(cluster_time)
     2000    0.001    0.000    0.001    0.000 client_session.py:699(_advance_cluster_time)
     2000    0.001    0.000    0.001    0.000 client_session.py:722(_advance_operation_time)
     2000    0.003    0.000    0.006    0.000 client_session.py:743(_process_response)
    12000    0.004    0.000    0.008    0.000 client_session.py:757(in_transaction)
     2000    0.001    0.000    0.001    0.000 client_session.py:765(_pinned_address)
     2000    0.004    0.000    0.010    0.000 client_session.py:787(_apply_to)
     2000    0.001    0.000    0.002    0.000 client_session.py:826(_start_retryable_write)
     6000    0.004    0.000    0.005    0.000 client_session.py:848(timed_out)
     2000    0.001    0.000    0.001    0.000 client_session.py:859(inc_transaction_id)
     2000    0.002    0.000    0.006    0.000 client_session.py:882(get_server_session)
     2000    0.002    0.000    0.006    0.000 client_session.py:898(return_server_session)
     2000    0.002    0.000    0.002    0.000 client_session.py:903(return_server_session_no_lock)
     4000    0.002    0.000    0.004    0.000 client_session.py:910(_clear_stale)
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:281(getstate)
     2000    0.000    0.000    0.000    0.000 collection.py:314(name)
     2000    0.008    0.000    0.763    0.000 collection.py:559(_insert_one)
     2000    0.005    0.000    0.493    0.000 collection.py:578(_insert_command)
     2000    0.002    0.000    0.766    0.000 collection.py:608(_insert)
     2000    0.005    0.000    0.782    0.000 collection.py:654(insert_one)
     2000    0.001    0.000    0.009    0.000 common.py:499(validate_is_document_type)
     2000    0.000    0.000    0.000    0.000 common.py:838(write_concern)
     2000    0.001    0.000    0.001    0.000 common.py:848(_write_concern_for)
6000/4000    0.005    0.000    0.065    0.000 contextlib.py:107(__enter__)
6000/4000    0.008    0.000    0.084    0.000 contextlib.py:116(__exit__)
     6000    0.004    0.000    0.013    0.000 contextlib.py:237(helper)
     6000    0.008    0.000    0.009    0.000 contextlib.py:81(__init__)
       16    0.000    0.000    0.000    0.000 cp1252.py:22(decode)
     4000    0.001    0.000    0.001    0.000 database.py:156(client)
     2000    0.000    0.000    0.000    0.000 database.py:161(name)
     2000    0.010    0.000    0.010    0.000 errors.py:103(_format_detailed_error)
     2000    0.004    0.000    0.018    0.000 errors.py:154(__init__)
     2000    0.000    0.000    0.000    0.000 errors.py:168(code)
     6000    0.001    0.000    0.001    0.000 errors.py:174(details)
     2000    0.004    0.000    0.004    0.000 errors.py:33(__init__)
     4000    0.001    0.000    0.001    0.000 errors.py:38(has_error_label)
        1    0.000    0.000    0.000    0.000 genericpath.py:27(isfile)
     2000    0.001    0.000    0.001    0.000 helpers.py:105(_check_command_response)
     2000    0.003    0.000    0.021    0.000 helpers.py:202(_raise_last_write_error)
     2000    0.001    0.000    0.023    0.000 helpers.py:220(_check_write_command_response)
        3    0.000    0.000    0.000    0.000 iostream.py:197(schedule)
        2    0.000    0.000    0.000    0.000 iostream.py:310(_is_master_process)
        2    0.000    0.000    0.000    0.000 iostream.py:323(_schedule_flush)
        2    0.000    0.000    0.000    0.000 iostream.py:386(write)
        3    0.000    0.000    0.000    0.000 iostream.py:93(_event_pipe)
        1    0.006    0.006    0.799    0.799 main.py:33(load_users)
     2000    0.001    0.000    0.001    0.000 message.py:1596(__init__)
     2000    0.002    0.000    0.017    0.000 message.py:1603(unpack_response)
     2000    0.001    0.000    0.001    0.000 message.py:1626(more_to_come)
     2000    0.005    0.000    0.008    0.000 message.py:1631(unpack)
     2000    0.008    0.000    0.064    0.000 message.py:692(_op_msg)
     2000    0.001    0.000    0.001    0.000 mongo_client.py:1131(retry_writes)
     2000    0.002    0.000    0.023    0.000 mongo_client.py:1232(_get_topology)
     4000    0.009    0.000    0.091    0.000 mongo_client.py:1243(_get_socket)
     2000    0.004    0.000    0.058    0.000 mongo_client.py:1257(_select_server)
     2000    0.003    0.000    0.677    0.000 mongo_client.py:1374(_retry_with_session)
     2000    0.011    0.000    0.671    0.000 mongo_client.py:1386(_retry_internal)
     2000    0.000    0.000    0.000    0.000 mongo_client.py:1392(is_retrying)
     2000    0.004    0.000    0.737    0.000 mongo_client.py:1495(_retryable_write)
     2000    0.006    0.000    0.022    0.000 mongo_client.py:1756(__start_session)
     2000    0.001    0.000    0.012    0.000 mongo_client.py:1800(_get_server_session)
     2000    0.001    0.000    0.010    0.000 mongo_client.py:1804(_return_server_session)
     2000    0.001    0.000    0.024    0.000 mongo_client.py:1808(_ensure_session)
     4000    0.004    0.000    0.045    0.000 mongo_client.py:1821(_tmp_session)
     2000    0.002    0.000    0.003    0.000 mongo_client.py:1847(_send_cluster_time)
     2000    0.003    0.000    0.012    0.000 mongo_client.py:1860(_process_response)
     2000    0.003    0.000    0.004    0.000 mongo_client.py:2269(__init__)
     2000    0.001    0.000    0.001    0.000 mongo_client.py:2281(contribute_socket)
     2000    0.000    0.000    0.000    0.000 mongo_client.py:2287(__enter__)
     2000    0.006    0.000    0.024    0.000 mongo_client.py:2290(__exit__)
     2000    0.001    0.000    0.008    0.000 monitor.py:79(open)
     2000    0.000    0.000    0.000    0.000 monitoring.py:1215(enabled_for_commands)
     2000    0.007    0.000    0.295    0.000 network.py:186(receive_message)
     4000    0.001    0.000    0.001    0.000 network.py:227(wait_for_read)
     4000    0.011    0.000    0.279    0.000 network.py:279(_receive_data_on_socket)
     2000    0.017    0.000    0.437    0.000 network.py:43(command)
     4000    0.005    0.000    0.012    0.000 periodic_executor.py:57(open)
     4000    0.003    0.000    0.042    0.000 pool.py:1204(get_socket)
     2000    0.006    0.000    0.016    0.000 pool.py:1246(_get_socket)
     2000    0.007    0.000    0.022    0.000 pool.py:1303(return_socket)
     2000    0.002    0.000    0.004    0.000 pool.py:1332(_perished)
     2000    0.000    0.000    0.000    0.000 pool.py:384(max_idle_time_seconds)
     2000    0.000    0.000    0.000    0.000 pool.py:404(wait_queue_timeout)
     4000    0.001    0.000    0.001    0.000 pool.py:437(event_listeners)
     2000    0.010    0.000    0.465    0.000 pool.py:612(command)
     2000    0.000    0.000    0.000    0.000 pool.py:728(_raise_if_not_writable)
     2000    0.001    0.000    0.001    0.000 pool.py:774(check_auth)
     2000    0.001    0.000    0.001    0.000 pool.py:816(validate_session)
     2000    0.001    0.000    0.004    0.000 pool.py:859(send_cluster_time)
     2000    0.001    0.000    0.001    0.000 pool.py:864(update_last_checkin_time)
     2000    0.000    0.000    0.000    0.000 pool.py:867(update_is_writable)
     2000    0.001    0.000    0.001    0.000 pool.py:870(idle_time_seconds)
     2000    0.001    0.000    0.002    0.000 py3compat.py:49(itervalues)
     2000    0.002    0.000    0.004    0.000 random.py:224(_randbelow)
     2000    0.002    0.000    0.006    0.000 random.py:256(choice)
     2000    0.002    0.000    0.002    0.000 read_preferences.py:121(document)
     2000    0.001    0.000    0.005    0.000 server.py:198(get_socket)
     8000    0.001    0.000    0.001    0.000 server.py:201(description)
     4000    0.000    0.000    0.000    0.000 server.py:210(pool)
     2000    0.001    0.000    0.009    0.000 server.py:44(open)
     2000    0.001    0.000    0.001    0.000 server_description.py:195(mongos)
     2000    0.001    0.000    0.002    0.000 server_description.py:199(is_server_type_known)
     2000    0.001    0.000    0.001    0.000 server_description.py:203(retryable_writes_supported)
     2000    0.000    0.000    0.000    0.000 server_description.py:215(topology_version)
     4000    0.001    0.000    0.001    0.000 server_description.py:84(address)
     2000    0.000    0.000    0.000    0.000 server_description.py:89(server_type)
     2000    0.000    0.000    0.000    0.000 settings.py:103(server_selection_timeout)
     2000    0.000    0.000    0.000    0.000 settings.py:107(server_selector)
        3    0.000    0.000    0.000    0.000 socket.py:432(send)
     2000    0.002    0.000    0.004    0.000 son.py:114(pop)
     4000    0.005    0.000    0.010    0.000 son.py:135(update)
     2000    0.002    0.000    0.013    0.000 son.py:40(__init__)
     2000    0.003    0.000    0.003    0.000 son.py:46(__new__)
    14000    0.010    0.000    0.011    0.000 son.py:57(__setitem__)
     2000    0.001    0.000    0.002    0.000 son.py:62(__delitem__)
    20000    0.003    0.000    0.003    0.000 son.py:77(__iter__)
     2000    0.003    0.000    0.005    0.000 thread_util.py:38(acquire)
     2000    0.003    0.000    0.010    0.000 thread_util.py:62(release)
     2000    0.001    0.000    0.011    0.000 thread_util.py:81(release)
     4003    0.002    0.000    0.003    0.000 threading.py:1050(_wait_for_tstate_lock)
     4003    0.003    0.000    0.007    0.000 threading.py:1092(is_alive)
     4000    0.001    0.000    0.002    0.000 threading.py:240(__enter__)
     4000    0.002    0.000    0.002    0.000 threading.py:243(__exit__)
     2000    0.001    0.000    0.001    0.000 threading.py:255(_is_owned)
     2000    0.003    0.000    0.004    0.000 threading.py:335(notify)
     4003    0.001    0.000    0.001    0.000 threading.py:507(is_set)
     2000    0.002    0.000    0.016    0.000 topology.py:145(open)
     2000    0.004    0.000    0.020    0.000 topology.py:174(select_servers)
     2000    0.001    0.000    0.003    0.000 topology.py:202(<listcomp>)
     2000    0.005    0.000    0.014    0.000 topology.py:205(_select_servers_loop)
     2000    0.002    0.000    0.029    0.000 topology.py:236(select_server)
     2000    0.001    0.000    0.001    0.000 topology.py:353(get_server_by_address)
     2000    0.000    0.000    0.000    0.000 topology.py:395(max_cluster_time)
     2000    0.000    0.000    0.000    0.000 topology.py:399(_receive_cluster_time_no_lock)
     2000    0.002    0.000    0.003    0.000 topology.py:413(receive_cluster_time)
     2000    0.003    0.000    0.011    0.000 topology.py:477(get_server_session)
     2000    0.003    0.000    0.009    0.000 topology.py:502(return_server_session)
     2000    0.002    0.000    0.013    0.000 topology.py:521(_ensure_opened)
     2000    0.006    0.000    0.009    0.000 topology.py:543(_is_stale_error)
     2000    0.004    0.000    0.014    0.000 topology.py:563(_handle_error)
     2000    0.001    0.000    0.016    0.000 topology.py:612(handle_error)
     2000    0.001    0.000    0.001    0.000 topology.py:754(__init__)
     2000    0.000    0.000    0.000    0.000 topology.py:762(_is_stale_error_topology_version)
     2000    0.000    0.000    0.000    0.000 topology_description.py:118(check_compatible)
     2000    0.000    0.000    0.000    0.000 topology_description.py:159(topology_type)
     6000    0.001    0.000    0.001    0.000 topology_description.py:187(logical_session_timeout_minutes)
     2000    0.002    0.000    0.005    0.000 topology_description.py:192(known_servers)
     2000    0.001    0.000    0.003    0.000 topology_description.py:195(<listcomp>)
     2000    0.003    0.000    0.008    0.000 topology_description.py:222(apply_selector)
     2000    0.009    0.000    0.791    0.000 users.py:21(add_user)
     8000    0.001    0.000    0.001    0.000 write_concern.py:104(acknowledged)
     4000    0.001    0.000    0.001    0.000 write_concern.py:89(is_server_default)
     2000    0.001    0.000    0.001    0.000 {built-in method __new__ of type object at 0x00007FFF3F1279A0}
    14000    0.006    0.000    0.010    0.000 {built-in method _abc._abc_instancecheck}
     2000    0.002    0.000    0.003    0.000 {built-in method _abc._abc_subclasscheck}
       16    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_decode}
        1    0.000    0.000    0.000    0.000 {built-in method _csv.reader}
        1    0.000    0.000    0.000    0.000 {built-in method _locale._getdefaultlocale}
        1    0.000    0.000    0.000    0.000 {built-in method _stat.S_ISREG}
     2000    0.013    0.000    0.013    0.000 {built-in method bson._cbson.decode_all}
        1    0.000    0.000    0.799    0.799 {built-in method builtins.exec}
     8000    0.001    0.000    0.001    0.000 {built-in method builtins.getattr}
    10000    0.002    0.000    0.002    0.000 {built-in method builtins.hasattr}
    12002    0.004    0.000    0.012    0.000 {built-in method builtins.isinstance}
    12000    0.001    0.000    0.001    0.000 {built-in method builtins.issubclass}
     6000    0.002    0.000    0.002    0.000 {built-in method builtins.iter}
     8000    0.001    0.000    0.001    0.000 {built-in method builtins.len}
10000/8000    0.003    0.000    0.063    0.000 {built-in method builtins.next}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
     6002    0.001    0.000    0.001    0.000 {built-in method nt.getpid}
        1    0.000    0.000    0.000    0.000 {built-in method nt.stat}
     2000    0.036    0.000    0.042    0.000 {built-in method pymongo._cmessage._op_msg}
     6000    0.002    0.000    0.002    0.000 {built-in method sys.exc_info}
    14000    0.002    0.000    0.002    0.000 {built-in method time.monotonic}
     4000    0.001    0.000    0.001    0.000 {method '__enter__' of '_thread.lock' objects}
     4000    0.001    0.000    0.001    0.000 {method '__exit__' of '_thread.lock' objects}
     6003    0.002    0.000    0.002    0.000 {method 'acquire' of '_thread.lock' objects}
        3    0.000    0.000    0.000    0.000 {method 'append' of 'collections.deque' objects}
    14000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
     4000    0.001    0.000    0.001    0.000 {method 'appendleft' of 'collections.deque' objects}
     2000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    22000    0.003    0.000    0.003    0.000 {method 'get' of 'dict' objects}
     3997    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
     2000    0.000    0.000    0.000    0.000 {method 'gettimeout' of '_socket.socket' objects}
     2000    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
     4000    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.TextIOWrapper' objects}
     4000    0.266    0.000    0.266    0.000 {method 'recv_into' of '_socket.socket' objects}
     2000    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}
     2000    0.028    0.000    0.028    0.000 {method 'sendall' of '_socket.socket' objects}
6000/4000    0.004    0.000    0.078    0.000 {method 'throw' of 'generator' objects}
     2000    0.002    0.000    0.002    0.000 {method 'unpack' of 'Struct' objects}
     2000    0.001    0.000    0.001    0.000 {method 'unpack_from' of 'Struct' objects}
     6000    0.001    0.000    0.001    0.000 {method 'values' of 'dict' objects}