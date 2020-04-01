// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Waf
{
    public static partial class Invokes
    {
        /// <summary>
        /// `aws.waf.Rule` Retrieves a WAF Rule Resource Id.
        /// 
        /// 
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/waf_rule.html.markdown.
        /// </summary>
        [Obsolete("Use GetRule.InvokeAsync() instead")]
        public static Task<GetRuleResult> GetRule(GetRuleArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetRuleResult>("aws:waf/getRule:getRule", args ?? InvokeArgs.Empty, options.WithVersion());
    }
    public static class GetRule
    {
        /// <summary>
        /// `aws.waf.Rule` Retrieves a WAF Rule Resource Id.
        /// 
        /// 
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/waf_rule.html.markdown.
        /// </summary>
        public static Task<GetRuleResult> InvokeAsync(GetRuleArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetRuleResult>("aws:waf/getRule:getRule", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetRuleArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the WAF rule.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetRuleArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetRuleResult
    {
        public readonly string Name;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetRuleResult(
            string name,
            string id)
        {
            Name = name;
            Id = id;
        }
    }
}
